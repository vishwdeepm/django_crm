# Generated by Django 3.2.14 on 2022-07-14 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_alter_lead_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.CharField(choices=[('yt', 'YouTube'), ('google', 'Google'), ('fb', 'Facebook'), ('insta', 'Instagram'), ('newsL', 'Newsletter')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='special_files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
