# Generated by Django 3.0.7 on 2020-09-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
