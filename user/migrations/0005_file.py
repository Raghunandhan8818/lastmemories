# Generated by Django 5.1.1 on 2024-09-26 08:36

import django.db.models.deletion
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_memorialprofile_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=user.models.get_file_path)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('size', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('memorial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_files', to='user.memorialprofile')),
            ],
        ),
    ]
