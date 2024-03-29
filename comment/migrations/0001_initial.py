# Generated by Django 4.2.6 on 2024-02-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='名無し', max_length=100)),
                ('comment', models.CharField(max_length=500, verbose_name='内容')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='投稿日時')),
            ],
        ),
    ]
