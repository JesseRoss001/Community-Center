# Generated by Django 4.2.7 on 2023-12-01 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_userprofile_average_rating_rating_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]