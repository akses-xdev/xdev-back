import json

from django.db import migrations


def import_categories(app, _):
    Category = app.get_model("projects", "Category")

    with open("apps/projects/seed/categories/0000_categories.json", encoding="utf-8") as f:
        categories_data = json.load(f)

    for role_data in categories_data["categories"]:
        category_name = role_data["fields"]["name"]
        Category.objects.create(name=category_name)


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_categories, migrations.RunPython.noop)]