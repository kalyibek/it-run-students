# Generated by Django 5.0.1 on 2024-02-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='characteristics',
            field=models.TextField(null=True),
        ),
    ]