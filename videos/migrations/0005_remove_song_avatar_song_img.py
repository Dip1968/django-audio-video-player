# Generated by Django 4.0.1 on 2022-07-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_song_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='avatar',
        ),
        migrations.AddField(
            model_name='song',
            name='img',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]
