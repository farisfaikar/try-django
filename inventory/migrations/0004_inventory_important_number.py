# Generated by Django 4.1.5 on 2023-02-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventory_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='important_number',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
    ]
