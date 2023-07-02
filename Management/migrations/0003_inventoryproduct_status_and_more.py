# Generated by Django 4.2.1 on 2023-06-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryproduct',
            name='status',
            field=models.CharField(choices=[('ثبت شد', 'Submitted'), ('آماده ارسال', 'Ready to send')], default='ثبت شد', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='quantity',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(max_length=20),
        ),
    ]
