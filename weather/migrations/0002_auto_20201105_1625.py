# Generated by Django 3.1.3 on 2020-11-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='wearther',
            new_name='weather',
        ),
    ]