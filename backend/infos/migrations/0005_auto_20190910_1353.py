# Generated by Django 2.2.5 on 2019-09-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0004_auto_20190905_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewinfo',
            name='comment',
            field=models.CharField(max_length=50, null=True, verbose_name='备注说明'),
        ),
        migrations.AlterField(
            model_name='interviewinfo',
            name='num',
            field=models.SmallIntegerField(default=10, verbose_name='可预约人数'),
        ),
        migrations.AlterField(
            model_name='interviewinfo',
            name='tb_id',
            field=models.SmallIntegerField(verbose_name='预约时段(1:上午,2:下午)'),
        ),
    ]
