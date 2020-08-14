# Generated by Django 3.1 on 2020-08-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Transgender'), ('4', 'Not specify')], default='1', max_length=1),
            preserve_default=False,
        ),
    ]
