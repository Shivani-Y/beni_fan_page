# Generated by Django 3.0.3 on 2020-03-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
