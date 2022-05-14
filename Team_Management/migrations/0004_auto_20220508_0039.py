# Generated by Django 3.2.12 on 2022-05-07 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Team_Management', '0003_alter_team_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='Team_Management.profile'),
        ),
        migrations.AlterField(
            model_name='task',
            name='forUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TaskUser', to='Team_Management.profile'),
        ),
    ]
