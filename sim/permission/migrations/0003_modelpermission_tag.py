# Generated by Django 2.0.7 on 2018-07-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0002_modelpermission_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpermission',
            name='tag',
            field=models.CharField(default=None, max_length=1, null=True, verbose_name='tag'),
        ),
    ]