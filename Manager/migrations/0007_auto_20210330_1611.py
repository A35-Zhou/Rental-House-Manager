# Generated by Django 2.2.19 on 2021-03-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Manager', '0006_auto_20210330_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='inTime',
            field=models.DateField(verbose_name='入住时间'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='outTime',
            field=models.DateField(verbose_name='离开时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='inTime',
            field=models.DateField(verbose_name='入住时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='outTime',
            field=models.DateField(verbose_name='离开时间'),
        ),
    ]
