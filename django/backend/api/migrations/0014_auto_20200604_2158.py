# Generated by Django 3.0.2 on 2020-06-04 21:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200604_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='events_admins', to=settings.AUTH_USER_MODEL),
        ),
    ]
