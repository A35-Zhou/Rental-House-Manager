# Generated by Django 2.2.19 on 2021-03-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Manager', '0004_auto_20210328_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinfo',
            name='brand',
            field=models.FileField(default='HouseImg/brand/defaultBrand.png', upload_to='HouseImg/brand',
                                   verbose_name='公寓商标'),
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='houseImg',
            field=models.FileField(default='HouseImg/defaultHouse.png', upload_to='HouseImg', verbose_name='公寓照片'),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomImg',
            field=models.FileField(default='RoomImg/defaultRoom', upload_to='RoomImg', verbose_name='房间照片'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='typeImg',
            field=models.FileField(default='TypeImg/defaultType', upload_to='TypeImg', verbose_name='房型示例'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]