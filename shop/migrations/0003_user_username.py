# Generated by Django 3.2.4 on 2021-06-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210603_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='tushar', max_length=12),
        ),
    ]
