# Generated by Django 4.1.2 on 2023-05-11 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_pro_imglink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]