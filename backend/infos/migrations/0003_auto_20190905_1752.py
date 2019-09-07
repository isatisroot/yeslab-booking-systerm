# Generated by Django 2.2.5 on 2019-09-05 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('infos', '0002_auto_20190902_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservationinfo',
            options={'verbose_name': '实验预约信息表', 'verbose_name_plural': '实验预约信息表'},
        ),
        migrations.CreateModel(
            name='InterviewInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='预约日期')),
                ('tb_id', models.SmallIntegerField(verbose_name='预约时段')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.UserInfo')),
            ],
            options={
                'verbose_name_plural': '面试预约信息表',
                'verbose_name': '面试预约信息表',
                'db_table': 'interview',
            },
        ),
    ]