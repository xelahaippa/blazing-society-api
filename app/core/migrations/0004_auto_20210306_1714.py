# Generated by Django 2.1.15 on 2021-03-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_scoreline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreline',
            name='draw_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreline',
            name='first_player_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scoreline',
            name='second_player_score',
            field=models.IntegerField(default=0),
        ),
    ]
