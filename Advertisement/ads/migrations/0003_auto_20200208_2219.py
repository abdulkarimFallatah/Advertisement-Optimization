# Generated by Django 3.0.1 on 2020-02-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20200208_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='Related_website_url',
            field=models.CharField(max_length=200),
        ),
    ]
