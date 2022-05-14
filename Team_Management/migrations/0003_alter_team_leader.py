# Generated by Django 3.2.12 on 2022-05-07 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Team_Management', '0002_alter_team_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='Team_Management.profile'),
        ),
    ]
