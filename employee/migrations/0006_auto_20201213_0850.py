# Generated by Django 3.0 on 2020-12-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20201202_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
