# Generated by Django 3.2.12 on 2022-05-02 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Team_Management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currentTeam',
        ),
    ]
