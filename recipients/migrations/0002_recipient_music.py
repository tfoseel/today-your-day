# Generated by Django 5.1.7 on 2025-04-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='recipient_music/'),
        ),
    ]
