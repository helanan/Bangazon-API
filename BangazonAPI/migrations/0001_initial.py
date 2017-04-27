# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_last_active', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('expense_budget', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.Department')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type_provider', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=25)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_types', related_query_name='payment_types', to='BangazonAPI.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=100)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=45)),
                ('product_quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=25)),
                ('start_date', models.CharField(max_length=25)),
                ('end_date', models.CharField(max_length=25)),
                ('max_capacity', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.ProductType'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_types_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.PaymentType'),
        ),
        migrations.AddField(
            model_name='order',
            name='purchase_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BangazonAPI.Customer'),
        ),
    ]
