# Generated by Django 5.1.3 on 2024-12-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_bill_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
