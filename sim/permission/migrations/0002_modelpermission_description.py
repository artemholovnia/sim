# Generated by Django 2.0.7 on 2018-07-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpermission',
            name='description',
            field=models.CharField(default=None, max_length=256, null=True, verbose_name='description'),
        ),
    ]