# Generated by Django 5.0.6 on 2024-05-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='fallback.jpeg', upload_to='post-images'),
        ),
    ]
