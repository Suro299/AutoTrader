# Generated by Django 4.1.6 on 2023-06-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_detail_in_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtype',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
