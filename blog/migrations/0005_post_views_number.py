# Generated by Django 4.1.3 on 2023-01-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views_number',
            field=models.IntegerField(default=0),
        ),
    ]
