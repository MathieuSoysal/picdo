# Generated by Django 3.1.4 on 2021-02-24 07:56

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20210223_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to=gallery.models.get_picture_path),
        ),
    ]
