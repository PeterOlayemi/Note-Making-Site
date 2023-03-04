# Generated by Django 4.0.6 on 2022-08-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_alter_note_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.IntegerField(choices=[(0, 'DRAFT'), (1, 'PUBLISH')], default=1, help_text='Select Either Draft or Publish'),
        ),
    ]