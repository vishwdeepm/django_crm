# Generated by Django 3.2.14 on 2022-07-14 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20220714_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
