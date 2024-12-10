# Generated by Django 5.1.3 on 2024-12-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('specialization', models.CharField(max_length=50)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]