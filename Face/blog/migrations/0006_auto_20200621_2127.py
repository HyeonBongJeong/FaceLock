# Generated by Django 3.0.6 on 2020-06-21 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200621_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='doc',
            new_name='file',
        ),
    ]
