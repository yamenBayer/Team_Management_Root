# Generated by Django 3.2.12 on 2022-05-07 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Team_Management', '0004_auto_20220508_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Team Request', max_length=50)),
                ('state', models.BooleanField(default=False)),
                ('teamToJoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team_to_join', to='Team_Management.team')),
                ('userToJoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_to_join', to='Team_Management.profile')),
            ],
        ),
    ]
