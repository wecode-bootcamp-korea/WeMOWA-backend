# Generated by Django 3.0.6 on 2020-05-27 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200527_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('st_addr', models.CharField(max_length=300)),
                ('op_addr', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'prefixs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserWishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'users_wishlists',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Address')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'users_addresses',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(through='account.UserAddress', to='account.Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='prefix',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Prefix'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(through='account.UserWishlist', to='product.Product'),
        ),
        migrations.CreateModel(
            name='RegisteredLuggage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'db_table': 'registered_luggages',
            },
        ),
    ]