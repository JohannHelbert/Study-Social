# Generated by Django 4.2.6 on 2023-10-27 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_participans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='participans',
            new_name='participants',
        ),
    ]
