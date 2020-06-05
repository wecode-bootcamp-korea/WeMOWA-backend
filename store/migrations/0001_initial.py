# Generated by Django 3.0.6 on 2020-06-03 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'store_types',
            },
        ),
        migrations.CreateModel(
            name='StoreStoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Store')),
                ('store_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.StoreType')),
            ],
            options={
                'db_table': 'store_store_types',
            },
        ),
        migrations.AddField(
            model_name='store',
            name='store_type',
            field=models.ManyToManyField(through='store.StoreStoreType', to='store.StoreType'),
        ),
    ]
