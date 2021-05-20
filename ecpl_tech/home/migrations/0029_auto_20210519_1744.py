# Generated by Django 3.1.7 on 2021-05-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_id', models.IntegerField()),
                ('email', models.EmailField(default='emp@ecpl.com', max_length=254, null=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='P',
        ),
    ]