# Generated by Django 4.2.2 on 2023-09-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mail',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
