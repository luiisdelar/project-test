# Generated by Django 3.2.7 on 2021-09-27 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_remove_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymoususer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
