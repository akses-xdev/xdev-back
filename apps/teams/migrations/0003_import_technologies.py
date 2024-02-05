import json

from django.db import migrations


def import_technologies(app, _):
    Technology = app.get_model("teams", "Technology")

    with open("apps/teams/seed/technologies/0000_technologies.json", encoding="utf-8") as f:
        technologies_data = json.load(f)

    for technology_data in technologies_data["technologies"]:
        technology_name = technology_data["fields"]["name"]
        Technology.objects.create(name=technology_name)


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0002_import_roles"),
    ]

    operations = [migrations.RunPython(import_technologies, migrations.RunPython.noop)]