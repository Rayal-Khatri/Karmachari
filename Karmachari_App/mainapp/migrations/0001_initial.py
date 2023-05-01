# Generated by Django 4.1.3 on 2023-04-27 19:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Everyone', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100, null=True)),
                ('hourly_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_start', models.TimeField()),
                ('schedule_end', models.TimeField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimg', models.ImageField(default='img.png', upload_to='profile_images')),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(default=0, max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.salary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_pay', models.DecimalField(decimal_places=2, default=10000, max_digits=8)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('deductions', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('net_pay', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('context', models.TextField(max_length=100000, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.DateField(default=django.utils.timezone.now)),
                ('leave_type', models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Vacation', 'Vacation'), ('Emergency', 'Emergency')], max_length=100, null=True)),
                ('message', models.TextField(max_length=100000, null=True)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Not Approved', 'Not Approved')], default='Pending', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_status', models.CharField(max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_id', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfQuestion', models.DateField(null=True)),
                ('checkInTime', models.DateTimeField(null=True)),
                ('checkOutTime', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('duration', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('Late', 'Late'), ('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave'), ('Holiday', 'Holiday')], max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
