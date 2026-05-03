from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from .models import Subscription, User


for model in (Group, TokenProxy):
    try:
        admin.site.unregister(model)
    except NotRegistered:
        pass


@admin.register(User)
class FoodgramUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user__username', 'author__username')
