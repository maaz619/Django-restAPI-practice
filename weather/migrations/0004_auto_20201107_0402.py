# Generated by Django 3.1.3 on 2020-11-07 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20201107_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='currentTime',
            new_name='createdAt',
        ),
    ]
