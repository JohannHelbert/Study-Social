# Generated by Django 3.2.23 on 2023-11-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.png', null=True, upload_to=''),
        ),
    ]
