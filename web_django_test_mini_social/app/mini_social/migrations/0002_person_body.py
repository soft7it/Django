# Generated by Django 4.2.2 on 2023-06-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='body',
            field=models.CharField(default='', max_length=200),
        ),
    ]
