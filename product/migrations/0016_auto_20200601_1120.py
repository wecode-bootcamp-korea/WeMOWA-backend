# Generated by Django 3.0.6 on 2020-06-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200531_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='text',
        ),
        migrations.AddField(
            model_name='productoption',
            name='tag_text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
