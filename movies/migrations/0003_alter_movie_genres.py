# Generated by Django 5.0.1 on 2024-01-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre', verbose_name='жанры'),
        ),
    ]
