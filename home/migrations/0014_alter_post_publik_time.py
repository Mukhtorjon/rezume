# Generated by Django 4.2.2 on 2023-09-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publik_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
