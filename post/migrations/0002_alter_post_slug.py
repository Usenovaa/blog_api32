# Generated by Django 4.2.9 on 2024-02-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
