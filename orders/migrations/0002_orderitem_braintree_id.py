# Generated by Django 3.2 on 2021-05-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
