# Generated by Django 4.0 on 2021-12-31 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstaBook', '0002_user_uploads_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_uploads',
            name='comments',
            field=models.TextField(default=''),
        ),
    ]