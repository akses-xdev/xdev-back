# Generated by Django 4.2.9 on 2024-05-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_import_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
