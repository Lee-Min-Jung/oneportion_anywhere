# Generated by Django 3.2.6 on 2021-08-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0004_auto_20210807_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, default='loaddish.jpg', upload_to='images/'),
        ),
    ]
