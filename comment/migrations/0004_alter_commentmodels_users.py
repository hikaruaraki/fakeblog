# Generated by Django 4.2.6 on 2024-03-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_commentmodels_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodels',
            name='users',
            field=models.CharField(max_length=100, verbose_name='ユーザ名'),
        ),
    ]
