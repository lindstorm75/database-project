# Generated by Django 3.1 on 2020-11-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databasesite', '0002_auto_20201128_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
