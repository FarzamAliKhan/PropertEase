# Generated by Django 4.2 on 2023-07-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_remove_location_city_alter_listing_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[(None, None), ('Karachi', 'Karachi'), ('Lahore', 'Lahore'), ('Islamabad', 'Islamabad'), ('Faisalabad', 'Faisalabad'), ('Hyderabad', 'Hyderabad'), ('Peshawar', 'Peshawar'), ('Quetta', 'Quetta'), ('Rawalpindi', 'Rawalpindi'), ('Multan', 'Multan'), ('Gujranwala', 'Gujranwala')], max_length=150, null=True),
        ),
    ]
