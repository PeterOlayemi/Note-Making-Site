# Generated by Django 4.0.6 on 2022-08-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_alter_note_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'DRAFT'), (2, 'PUBLISH')], default=0, help_text='Select Either Draft or Publish'),
        ),
    ]
