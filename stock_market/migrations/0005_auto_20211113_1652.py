# Generated by Django 3.2.7 on 2021-11-13 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_market', '0004_stockfoliouser_stockportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockportfolio',
            name='earnt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stockportfolio',
            name='net',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stockportfolio',
            name='spent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='stockportfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StockFolioUser',
        ),
    ]