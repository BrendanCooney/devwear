# Generated by Django 3.2.23 on 2024-03-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
