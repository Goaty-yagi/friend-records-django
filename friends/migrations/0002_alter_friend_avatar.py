# Generated by Django 4.2.2 on 2023-07-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='avatar',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
