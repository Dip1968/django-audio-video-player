# Generated by Django 4.0.1 on 2022-07-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_delete_thumb_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]