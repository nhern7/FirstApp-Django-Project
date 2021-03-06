# Generated by Django 3.2 on 2021-05-30 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='guides',
            field=models.ForeignKey(default=1, limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='travello.guide'),
        ),
        migrations.AddField(
            model_name='guide',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
