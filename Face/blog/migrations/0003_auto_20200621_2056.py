# Generated by Django 3.0.6 on 2020-06-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200621_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='doc',
            field=models.FileField(upload_to='blog/'),
        ),
    ]
