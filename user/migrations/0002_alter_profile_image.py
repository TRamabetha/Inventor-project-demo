# Generated by Django 4.1.7 on 2023-03-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profileimage.png', upload_to='Profile_Images'),
        ),
    ]
