# Generated by Django 3.0.2 on 2020-01-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200127_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Опубликовано'),
        ),
    ]
