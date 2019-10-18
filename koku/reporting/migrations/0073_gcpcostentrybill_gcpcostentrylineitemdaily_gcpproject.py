# Generated by Django 2.2.4 on 2019-10-18 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20191008_1905'),
        ('reporting', '0072_auto_20191011_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='GCPCostEntryBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_period_start', models.DateTimeField()),
                ('billing_period_end', models.DateTimeField()),
                ('summary_data_creation_datetime', models.DateTimeField(null=True)),
                ('summary_data_updated_datetime', models.DateTimeField(null=True)),
                ('finalized_datetime', models.DateTimeField(null=True)),
                ('derived_cost_datetime', models.DateTimeField(null=True)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Provider')),
            ],
            options={
                'unique_together': {('billing_period_start', 'provider')},
            },
        ),
        migrations.CreateModel(
            name='GCPProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=20)),
                ('project_number', models.BigIntegerField()),
                ('project_id', models.CharField(max_length=256, unique=True)),
                ('project_name', models.CharField(max_length=256)),
                ('project_labels', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GCPCostEntryLineItemDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_item_type', models.CharField(max_length=256)),
                ('measurement_type', models.CharField(max_length=512)),
                ('consumption', models.BigIntegerField()),
                ('unit', models.CharField(max_length=63, null=True)),
                ('cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('currency', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=256)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('cost_entry_bill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reporting.GCPCostEntryBill')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reporting.GCPProject')),
            ],
        ),
    ]