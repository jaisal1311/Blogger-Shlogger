# Generated by Django 3.0.3 on 2020-06-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200615_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default', upload_to='images'),
        ),
    ]
