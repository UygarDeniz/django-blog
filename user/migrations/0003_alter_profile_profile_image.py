# Generated by Django 5.1.4 on 2024-12-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_bio_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/profile_pics/default_profile_pic.jpg', upload_to=''),
        ),
    ]
