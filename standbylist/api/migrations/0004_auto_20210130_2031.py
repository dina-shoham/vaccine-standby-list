# Generated by Django 3.1.5 on 2021-01-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_patient_riskfactors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='riskFactors',
            field=models.IntegerField(default=0),
        ),
    ]