# Generated by Django 3.1.6 on 2021-07-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poszukiwania', '0003_auto_20210712_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzeczy',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]