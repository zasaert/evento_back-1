# Generated by Django 5.0.3 on 2024-04-03 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user'},
        ),
    ]