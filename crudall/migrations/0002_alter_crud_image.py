# Generated by Django 4.2.6 on 2024-04-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='Image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
