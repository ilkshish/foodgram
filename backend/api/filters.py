import django_filters

from recipes.models import Recipe, Tag


class RecipeFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )
    is_favorited = django_filters.NumberFilter(method='filter_is_favorited')
    is_in_shopping_cart = django_filters.NumberFilter(
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('author', 'tags')

    def filter_is_favorited(self, queryset, name, value):
        user = getattr(self.request, 'user', None)
        if value != 1 or user is None or user.is_anonymous:
            return queryset
        return queryset.filter(favorited_by__user=user)

    def filter_is_in_shopping_cart(self, queryset, name, value):
        user = getattr(self.request, 'user', None)
        if value != 1 or user is None or user.is_anonymous:
            return queryset
        return queryset.filter(in_shopping_carts__user=user)
