# Generated by Django 5.0.6 on 2024-05-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=2, max_length=98),
            preserve_default=False,
        ),
    ]