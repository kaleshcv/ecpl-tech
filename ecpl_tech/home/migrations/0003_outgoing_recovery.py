# Generated by Django 3.1.7 on 2021-07-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210616_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outgoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('serial_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('serial_no', models.CharField(max_length=100)),
            ],
        ),
    ]
