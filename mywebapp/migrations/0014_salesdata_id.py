# Generated by Django 3.2.4 on 2021-06-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0013_auto_20210616_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdata',
            name='id',
            field=models.IntegerField(default=0),
        ),
    ]
