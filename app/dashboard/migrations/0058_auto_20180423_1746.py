# Generated by Django 2.0.4 on 2018-04-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0057_auto_20180419_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='bountyfulfillment',
            name='fulfiller_hours_worked',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
