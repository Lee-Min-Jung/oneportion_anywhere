# Generated by Django 3.2 on 2021-08-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('일상공유', '일상공유'), ('레시피공유', '레시피공유')], default='일상공유', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]