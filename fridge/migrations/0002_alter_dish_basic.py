# Generated by Django 3.2.6 on 2021-08-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='basic',
            field=models.TextField(blank=True, default='없음', max_length=200, null=True),
        ),
    ]