# Generated by Django 5.1.3 on 2024-11-29 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_shoes_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='shoes',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoes.brand'),
        ),
    ]
