# Generated by Django 4.1 on 2022-08-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]