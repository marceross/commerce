# Generated by Django 4.2.6 on 2023-11-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_bids_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
