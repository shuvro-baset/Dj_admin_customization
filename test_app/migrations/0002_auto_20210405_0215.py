# Generated by Django 3.1.7 on 2021-04-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(),
        ),
    ]
