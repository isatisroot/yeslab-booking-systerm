# Generated by Django 2.2.3 on 2019-09-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationinfo',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='date',
            field=models.DateField(verbose_name='预约日期'),
        ),
    ]
