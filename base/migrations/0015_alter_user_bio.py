# Generated by Django 4.0.2 on 2022-02-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_user_workplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
