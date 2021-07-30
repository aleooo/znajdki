# Generated by Django 3.1.6 on 2021-07-30 16:12

from django.conf import settings
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
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.JSONField(null=True)),
                ('description', models.CharField(blank=True, default='Znajdka', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rzeczy',
            fields=[
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='poszukiwania.map')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, unique_for_date='publish')),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image_obverse', models.ImageField(default='empty.png', upload_to='rzeczy/%Y/%m/%d', verbose_name='image_obverse')),
                ('image_reverse', models.ImageField(default='empty.png', upload_to='rzeczy/%Y/%m/%d', verbose_name='image_revers')),
                ('comments', models.TextField(blank=True, null=True)),
                ('catalog_number', models.PositiveSmallIntegerField(default=0)),
                ('update', models.DateField(auto_now=True)),
                ('publish', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rzeczy', to='poszukiwania.category')),
                ('user', models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['publish'],
            },
        ),
    ]
