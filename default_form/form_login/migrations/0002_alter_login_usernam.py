# Generated by Django 3.2.7 on 2021-09-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='usernam',
            field=models.CharField(max_length=100),
        ),
    ]