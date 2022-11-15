# Generated by Django 3.2 on 2022-10-26 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('sendBy', models.CharField(max_length=10)),
                ('receiver', models.CharField(max_length=10)),
                ('dateReceiver', models.DateTimeField(default=django.utils.timezone.now)),
                ('validateMP', models.BooleanField(default=False)),
                ('validateRH', models.BooleanField(default=False)),
                ('validateAS', models.BooleanField(default=False)),
                ('validateRT', models.BooleanField(default=False)),
            ],
        ),
    ]
