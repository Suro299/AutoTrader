# Generated by Django 4.1.6 on 2023-06-17 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_detail_in_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='in_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.car'),
        ),
    ]
