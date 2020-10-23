# Generated by Django 3.0.8 on 2020-10-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20200812_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='round',
            new_name='format',
        ),
        migrations.AddField(
            model_name='course',
            name='format',
            field=models.CharField(blank=True, choices=[('flint', 'IFAA Flint'), ('indoor', 'IFAA Indoor'), ('animal', 'IFAA Animal (Marked Distances)'), ('field', 'IFAA Field'), ('hunter', 'IFAA Hunter')], max_length=255, verbose_name='Format'),
        ),
        migrations.AddField(
            model_name='event',
            name='age_style_used',
            field=models.TextField(blank=True, verbose_name='age_style classes used in the event'),
        ),
        migrations.AddField(
            model_name='scorecard',
            name='spots',
            field=models.IntegerField(default=None, null=True, verbose_name='nr of "x" or equivalent'),
        ),
        migrations.AlterField(
            model_name='levelclass',
            name='age_group',
            field=models.CharField(choices=[('C', 'Cub'), ('J', 'Junior'), ('Y', 'Young Adult'), ('A', 'Adult'), ('V', 'Veteran'), ('S', 'Senior')], max_length=1, verbose_name='age group'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='age_group',
            field=models.CharField(choices=[('C', 'Cub'), ('J', 'Junior'), ('Y', 'Young Adult'), ('A', 'Adult'), ('V', 'Veteran'), ('S', 'Senior')], max_length=1, verbose_name='age group'),
        ),
        migrations.AlterField(
            model_name='record',
            name='age_group',
            field=models.CharField(choices=[('C', 'Cub'), ('J', 'Junior'), ('Y', 'Young Adult'), ('A', 'Adult'), ('V', 'Veteran'), ('S', 'Senior')], max_length=1, verbose_name='age group'),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('format', 'age_group', 'gender', 'style', 'scope', 'date')},
        ),
        migrations.AlterField(
            model_name='record',
            name='format',
            field=models.CharField(choices=[('flint', 'IFAA Flint'), ('indoor', 'IFAA Indoor'), ('animal', 'IFAA Animal (Marked Distances)'), ('field', 'IFAA Field'), ('hunter', 'IFAA Hunter')], max_length=255, verbose_name='Format'),
        ),
    ]
