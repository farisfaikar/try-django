# Generated by Django 4.1.5 on 2023-02-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_inventory_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='content',
            field=models.TextField(default='i did an oopsie'),
            preserve_default=False,
        ),
    ]