# Generated by Django 4.0.6 on 2022-08-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='entry',
            field=models.TextField(help_text="Enter Note's Entry"),
        ),
    ]
