# Generated by Django 3.0.6 on 2020-06-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200623_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(default='내용이 없습니다.'),
        ),
    ]
