# Generated by Django 3.1.7 on 2021-03-24 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0002_recipe_preparation_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="name",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
