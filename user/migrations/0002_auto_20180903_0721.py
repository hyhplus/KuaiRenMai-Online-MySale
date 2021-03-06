# Generated by Django 2.1 on 2018-09-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='wechat',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='brand',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='collect',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='company',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='job',
            field=models.CharField(default='', max_length=20),
        ),
    ]
