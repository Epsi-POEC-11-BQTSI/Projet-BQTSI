# Generated by Django 3.2 on 2022-11-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0016_auto_20221110_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='message.service'),
        ),
    ]
