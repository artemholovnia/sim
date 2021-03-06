# Generated by Django 2.0.7 on 2018-07-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default=None, max_length=128, null=True, verbose_name='model name')),
                ('permission_name', models.CharField(default=None, max_length=128, null=True, verbose_name='permission name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'db_table': 'model_permissions',
            },
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=16, unique=True, verbose_name='name')),
                ('permissions', models.CharField(blank=True, default=None, editable=False, max_length=512, null=True, verbose_name='permissions')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('model_permissions', models.ManyToManyField(to='permission.ModelPermission', verbose_name='model permissions')),
            ],
            options={
                'db_table': 'permission_groups',
            },
        ),
    ]
