# Generated by Django 3.2.7 on 2021-09-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_alter_anonymoususer_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymoususer',
            name='created_date',
            field=models.DateField(),
        ),
    ]