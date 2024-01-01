# Generated by Django 4.2 on 2023-07-16 00:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0011_rename_user_listing_created_by_listing_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]