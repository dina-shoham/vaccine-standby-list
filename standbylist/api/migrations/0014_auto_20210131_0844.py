# Generated by Django 2.2.12 on 2021-01-31 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210131_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Clinic'),
        ),
    ]