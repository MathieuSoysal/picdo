# Generated by Django 3.1.4 on 2021-02-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_picture_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
