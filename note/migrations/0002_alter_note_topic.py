# Generated by Django 4.0.6 on 2022-08-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='topic',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
