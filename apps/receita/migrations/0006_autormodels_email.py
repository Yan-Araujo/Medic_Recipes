# Generated by Django 4.2.5 on 2023-10-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0005_rename_autor_receitamodels_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='autormodels',
            name='email',
            field=models.EmailField(default='', max_length=40),
        ),
    ]
