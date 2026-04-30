import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает ингредиенты из CSV файла'

    def handle(self, *args, **options):
        file_path = (
            Path(__file__).resolve().parents[4] / 'data' / 'ingredients.csv'
        )

        if not file_path.exists():
            self.stdout.write(
                self.style.ERROR(f'Файл не найден: {file_path}')
            )
            return

        with open(file_path, encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            created_objects = Ingredient.objects.bulk_create(
                (
                    Ingredient(
                        name=name.strip(),
                        measurement_unit=measurement_unit.strip(),
                    )
                    for name, measurement_unit in reader
                    if name.strip() and measurement_unit.strip()
                ),
                ignore_conflicts=True,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Загрузка завершена. Добавлено ингредиентов: '
                f'{len(created_objects)}'
            )
        )
