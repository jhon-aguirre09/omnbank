# Generated by Django 2.2.5 on 2019-09-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.TextField(default='Null', max_length=80),
        ),
        migrations.AddField(
            model_name='movies',
            name='gener',
            field=models.TextField(default='drama', max_length=80),
        ),
    ]
