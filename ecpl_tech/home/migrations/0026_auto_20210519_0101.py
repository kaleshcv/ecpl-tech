# Generated by Django 3.1.7 on 2021-05-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20210519_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='doj',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
