# Generated by Django 3.2.7 on 2021-09-13 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='avalability',
            field=models.CharField(choices=[('danger', '午前中'), ('info', '午後'), ('success', '夜')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]