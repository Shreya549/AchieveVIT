# Generated by Django 3.1.1 on 2020-09-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
