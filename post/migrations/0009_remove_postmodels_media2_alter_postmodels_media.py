# Generated by Django 4.2.6 on 2024-02-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_postmodels_media2_alter_postmodels_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodels',
            name='media2',
        ),
        migrations.AlterField(
            model_name='postmodels',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='画像'),
        ),
    ]
