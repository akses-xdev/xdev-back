import json

from django.db import migrations


def import_roles(app, _):
    Role = app.get_model("teams", "Role")

    with open("apps/teams/seed/roles/0000_roles.json", encoding="utf-8") as f:
        roles_data = json.load(f)

    for role_data in roles_data["roles"]:
        role_name = role_data["fields"]["name"]
        Role.objects.create(name=role_name)


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_roles, migrations.RunPython.noop)]