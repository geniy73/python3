# Generated by Django 5.0.7 on 2024-07-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
