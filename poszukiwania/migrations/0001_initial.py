# Generated by Django 3.1.6 on 2021-05-31 08:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('description', models.TextField(blank=True, default='Znajdka')),
            ],
        ),
        migrations.CreateModel(
            name='Rzeczy',
            fields=[
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='poszukiwania.mapa')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, unique_for_date='publish')),
                ('year', models.PositiveIntegerField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='rzeczy/%Y/%m/%d')),
                ('publish', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rzeczy', to='poszukiwania.category')),
                ('user', models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['publish'],
            },
        ),
    ]
