# Generated by Django 3.2 on 2022-11-09 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_remove_message_file1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='motif',
            new_name='motif_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='receiver_id',
        ),
    ]
