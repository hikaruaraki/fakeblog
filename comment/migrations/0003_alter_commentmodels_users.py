# Generated by Django 4.2.6 on 2024-03-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_rename_published_date_commentmodels_publishe_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodels',
            name='users',
            field=models.CharField(max_length=100),
        ),
    ]
