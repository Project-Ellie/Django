# Generated by Django 2.2.6 on 2019-12-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191215_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
