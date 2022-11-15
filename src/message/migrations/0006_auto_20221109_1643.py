# Generated by Django 3.2 on 2022-11-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20221109_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='motif_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver_id',
        ),
        migrations.AddField(
            model_name='message',
            name='motif',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
