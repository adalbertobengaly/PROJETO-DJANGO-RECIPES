# Generated by Django 4.2.7 on 2024-08-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=65, verbose_name='Title'),
        ),
    ]
