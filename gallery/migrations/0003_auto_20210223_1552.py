# Generated by Django 3.1.4 on 2021-02-23 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210218_2316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['-date'], 'verbose_name': 'photo'},
        ),
    ]
