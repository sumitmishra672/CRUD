# Generated by Django 4.2.6 on 2024-04-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudall', '0002_alter_crud_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='description',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
