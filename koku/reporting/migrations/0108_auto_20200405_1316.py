# Generated by Django 2.2.11 on 2020-04-05 13:16
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "reporting",
            "0107_ocpazurecomputesummary_ocpazurecostsummary_ocpazurecostsummarybyaccount_ocpazurecostsummarybylocatio",
        )
    ]

    operations = [
        migrations.AlterModelTable(
            name="ocpawscostsummarybyservice", table="reporting_ocpaws_cost_summary_by_service"
        ),
        migrations.AlterModelTable(name="ocpazurecomputesummary", table="reporting_ocpazure_compute_summary"),
        migrations.AlterModelTable(name="ocpazurecostsummary", table="reporting_ocpazure_cost_summary"),
        migrations.AlterModelTable(
            name="ocpazurecostsummarybyaccount", table="reporting_ocpazure_cost_summary_by_account"
        ),
        migrations.AlterModelTable(
            name="ocpazurecostsummarybylocation", table="reporting_ocpazure_cost_summary_by_location"
        ),
        migrations.AlterModelTable(
            name="ocpazurecostsummarybyservice", table="reporting_ocpazure_cost_summary_by_service"
        ),
        migrations.AlterModelTable(name="ocpazuredatabasesummary", table="reporting_ocpazure_database_summary"),
        migrations.AlterModelTable(name="ocpazurenetworksummary", table="reporting_ocpazure_network_summary"),
        migrations.AlterModelTable(name="ocpazurestoragesummary", table="reporting_ocpazure_storage_summary"),
    ]
