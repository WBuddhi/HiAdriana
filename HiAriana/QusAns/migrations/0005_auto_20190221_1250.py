# Generated by Django 2.1.7 on 2019-02-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QusAns', '0004_auto_20190221_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qusjsonfile',
            name='TimeStamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='qusjsonfile',
            name='document',
            field=models.FileField(upload_to='Qusfiles/'),
        ),
    ]
