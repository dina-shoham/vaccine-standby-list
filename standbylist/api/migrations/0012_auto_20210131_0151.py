# Generated by Django 3.1.5 on 2021-01-31 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210131_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clinic'),
        ),
    ]
