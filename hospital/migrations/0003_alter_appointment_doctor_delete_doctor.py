# Generated by Django 5.1.3 on 2024-12-05 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('hospital', '0002_doctor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
