# Generated by Django 2.1.7 on 2019-02-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apistep',
            name='apistep',
            field=models.CharField(max_length=100, null=True, verbose_name='测试步骤'),
        ),
    ]