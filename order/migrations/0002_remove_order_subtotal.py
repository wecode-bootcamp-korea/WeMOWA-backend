# Generated by Django 3.0.6 on 2020-06-04 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subtotal',
        ),
    ]
