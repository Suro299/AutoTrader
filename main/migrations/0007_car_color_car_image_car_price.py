# Generated by Django 4.1.6 on 2023-06-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_detail_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'white'), ('black', 'black'), ('red', 'red'), ('blue', 'blue')], default='white', max_length=7),
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Pirce'),
        ),
    ]
