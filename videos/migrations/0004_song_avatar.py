# Generated by Django 4.0.1 on 2022-07-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
