# Generated by Django 3.0 on 2020-02-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0004_auto_20200204_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
