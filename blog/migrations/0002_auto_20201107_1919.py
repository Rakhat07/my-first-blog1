# Generated by Django 3.1.2 on 2020-11-07 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
    ]
