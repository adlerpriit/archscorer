# Generated by Django 3.0.2 on 2020-01-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200117_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='name_short',
            field=models.CharField(blank=True, default='***', max_length=5, verbose_name='Club name short'),
        ),
        migrations.AddField(
            model_name='club',
            name='association',
            field=models.CharField(blank=True, default='***', max_length=255, verbose_name='Association name (FAAE - in estonia)'),
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('archer', 'event', 'style', 'age_group')},
        ),
    ]