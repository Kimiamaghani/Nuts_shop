# Generated by Django 4.2.1 on 2023-06-03 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventoryproduct',
            name='Inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.inventory'),
        ),
        migrations.AddField(
            model_name='inventoryproduct',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.product'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.city'),
        ),
    ]