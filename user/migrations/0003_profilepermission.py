# Generated by Django 5.1.1 on 2024-09-25 17:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_plan_memorialprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(default='view', max_length=20)),
                ('memorial_profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='associated_memorial_profile', to='user.memorialprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='associated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
