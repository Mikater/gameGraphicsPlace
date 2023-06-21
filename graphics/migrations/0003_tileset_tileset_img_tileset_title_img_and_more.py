# Generated by Django 4.2 on 2023-06-14 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0002_tileset_alter_graphicpack_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='tileset',
            name='tileSet_img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tileset',
            name='title_img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='graphicpack',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 22, 34, 43, 361418)),
        ),
        migrations.AlterField(
            model_name='tileset',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 22, 34, 43, 362416)),
        ),
    ]