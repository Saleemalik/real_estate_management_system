# Generated by Django 5.0.1 on 2024-01-15 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('property_view', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('tenant_view', models.ImageField(blank=True, null=True, upload_to='tenants/')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_cost', models.FloatField(blank=True, null=True)),
                ('unit_type', models.CharField(blank=True, choices=[(1, '1BHK'), (2, '2BHK'), (3, '3BHK'), (4, '4BHK')], max_length=10, null=True)),
                ('unit_view', models.ImageField(blank=True, null=True, upload_to='untits/')),
                ('monthly_rent_date', models.DateField(blank=True, null=True)),
                ('agreement_end_date', models.DateField(blank=True, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.property')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.unit')),
            ],
        ),
    ]
