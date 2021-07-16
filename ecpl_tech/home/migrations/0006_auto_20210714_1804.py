# Generated by Django 3.1.7 on 2021-07-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210714_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outgoing',
            name='serial_no',
        ),
        migrations.RemoveField(
            model_name='recovery',
            name='serial_no',
        ),
        migrations.AddField(
            model_name='outgoing',
            name='campaign',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='emp_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='hard_disc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='hard_disc_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='hard_disc_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='headset',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='headset_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='it_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='make_model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='monitor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='pc_laptop',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='policy_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='processor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='ram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='remarks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='system_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outgoing',
            name='system_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='campaign',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='emp_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='emp_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='hard_disc_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='headset',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='headset_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='it_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='make_model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='monitor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='pc_laptop',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='policy_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='processor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='ram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='remarks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='system_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recovery',
            name='system_serial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='emp_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='emp_id',
            field=models.IntegerField(null=True),
        ),
    ]