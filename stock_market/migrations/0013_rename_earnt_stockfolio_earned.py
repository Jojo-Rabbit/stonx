# Generated by Django 3.2.7 on 2021-11-13 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_market', '0012_auto_20211113_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockfolio',
            old_name='earnt',
            new_name='earned',
        ),
    ]
