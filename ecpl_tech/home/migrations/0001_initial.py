# Generated by Django 3.1.7 on 2021-06-16 13:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='ACCESS', max_length=20)),
                ('item_id', models.IntegerField(default=8)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('item', models.CharField(max_length=50)),
                ('item_serial', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=50)),
                ('assigned_by', models.CharField(max_length=50)),
                ('campaign', models.CharField(max_length=100)),
                ('return_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Biometric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='BIOMETRIC', max_length=20)),
                ('item_id', models.IntegerField(default=17)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cctv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='CCTV', max_length=20)),
                ('item_id', models.IntegerField(default=14)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Converters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='CONVERTERS', max_length=20)),
                ('item_id', models.IntegerField(default=15)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='CPU', max_length=10)),
                ('item_id', models.IntegerField(default=1)),
                ('in_date', models.DateField()),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('processor', models.CharField(max_length=20)),
                ('ram', models.CharField(max_length=20)),
                ('hd_type', models.CharField(max_length=30)),
                ('hd_size', models.CharField(max_length=30)),
                ('hd_serial_no', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=50)),
                ('system_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=False)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='DESKTOP', max_length=20)),
                ('item_id', models.IntegerField(default=2)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('processor', models.CharField(max_length=20)),
                ('ram', models.CharField(max_length=20)),
                ('hd_type', models.CharField(max_length=30)),
                ('hd_size', models.CharField(max_length=30)),
                ('hd_serial_no', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=50)),
                ('system_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DvdWriter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='DVD', max_length=20)),
                ('item_id', models.IntegerField(default=13)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(null=True)),
                ('emp_name', models.CharField(max_length=50, null=True)),
                ('shift', models.CharField(max_length=15, null=True)),
                ('doj', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('process', models.TextField(null=True)),
                ('emp_desi', models.CharField(max_length=50, null=True)),
                ('personal_no', models.CharField(max_length=50, null=True)),
                ('emergency_no', models.CharField(max_length=50, null=True)),
                ('aadhar_no', models.CharField(max_length=50, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('address', models.TextField(null=True)),
                ('no_of_systems', models.IntegerField(null=True)),
                ('pc_or_lap', models.CharField(max_length=50, null=True)),
                ('make', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('serial', models.CharField(max_length=50, null=True)),
                ('ram', models.CharField(max_length=50, null=True)),
                ('hard_disc', models.CharField(max_length=50, null=True)),
                ('system_remarks', models.TextField(null=True)),
                ('inch_18', models.IntegerField(null=True)),
                ('inch_19', models.IntegerField(null=True)),
                ('inch_20', models.IntegerField(null=True)),
                ('inch_24', models.IntegerField(null=True)),
                ('monitor_remarks', models.TextField(null=True)),
                ('head_company', models.CharField(max_length=50, null=True)),
                ('head_own', models.CharField(max_length=10, null=True)),
                ('head_remarks', models.TextField(null=True)),
                ('keyboard', models.CharField(max_length=10, null=True)),
                ('mouse', models.CharField(max_length=10, null=True)),
                ('webcam', models.CharField(max_length=10, null=True)),
                ('other_remarks', models.TextField(null=True)),
                ('sophos', models.CharField(max_length=10, null=True)),
                ('connectwise', models.CharField(max_length=10, null=True)),
                ('vpn', models.CharField(max_length=10, null=True)),
                ('vpn_id', models.CharField(max_length=10, null=True)),
                ('call_date', models.DateTimeField(null=True)),
                ('called_by', models.CharField(max_length=50, null=True)),
                ('called_by_id', models.IntegerField(null=True)),
                ('emp_remarks', models.TextField(null=True)),
                ('data_collected', models.BooleanField(default=False)),
                ('agent_remarks', models.TextField(null=True)),
                ('number_error', models.BooleanField(default=False)),
                ('shift_error', models.BooleanField(default=False)),
                ('other_error', models.BooleanField(default=False)),
                ('other_error_remarks', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalHardDisc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='EHD', max_length=20)),
                ('item_id', models.IntegerField(default=18)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fortiget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='FORTIGET', max_length=20)),
                ('item_id', models.IntegerField(default=5)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='KEYBOARD', max_length=20)),
                ('item_id', models.IntegerField(default=11)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='LAPTOP', max_length=20)),
                ('item_id', models.IntegerField(default=4)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('processor', models.CharField(max_length=20)),
                ('ram', models.CharField(max_length=20)),
                ('hd_type', models.CharField(max_length=30)),
                ('hd_size', models.CharField(max_length=30)),
                ('hd_serial_no', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('battery_serial_no', models.CharField(max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('system_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='MONITOR', max_length=20)),
                ('item_id', models.IntegerField(default=3)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('screen_size', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='MOUSE', max_length=20)),
                ('item_id', models.IntegerField(default=10)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pendrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='PENDRIVE', max_length=20)),
                ('item_id', models.IntegerField(default=12)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='PRINTER', max_length=20)),
                ('item_id', models.IntegerField(default=9)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
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
        migrations.CreateModel(
            name='Projector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='PROJECTOR', max_length=20)),
                ('item_id', models.IntegerField(default=16)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnCpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('it_name', models.CharField(max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('item_serial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='ROUTER', max_length=20)),
                ('item_id', models.IntegerField(default=6)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('it_name', models.CharField(max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('item_serial', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('service_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='SPEAKER', max_length=20)),
                ('item_id', models.IntegerField(default=19)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='SWITCH', max_length=20)),
                ('item_id', models.IntegerField(default=7)),
                ('in_date', models.DateField(default=datetime.date.today)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('ecpl_tag_name', models.CharField(max_length=30, unique=True)),
                ('model_no', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField(default=True)),
                ('out', models.BooleanField(default=False)),
                ('assigned', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_id', models.IntegerField()),
                ('email', models.EmailField(default='emp@ecpl.com', max_length=254, null=True)),
                ('phone', models.IntegerField(default=999999999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
