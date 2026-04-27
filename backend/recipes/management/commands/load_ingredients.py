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

        ingredients_to_create = []

        with open(file_path, encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if len(row) < 2:
                    continue

                name = row[0].strip()
                measurement_unit = row[1].strip()

                if not name or not measurement_unit:
                    continue

                ingredients_to_create.append(
                    Ingredient(
                        name=name,
                        measurement_unit=measurement_unit
                    )
                )

        created_objects = Ingredient.objects.bulk_create(
            ingredients_to_create,
            ignore_conflicts=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Загрузка завершена. Добавлено ингредиентов: '
                f'{len(created_objects)}'
            )
        )
