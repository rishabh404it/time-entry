# Generated by Django 3.1.2 on 2020-10-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_logentry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='project',
            field=models.CharField(max_length=100),
        ),
    ]
