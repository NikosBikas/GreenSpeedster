# Generated by Django 4.0.2 on 2022-04-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size'), ('brand', 'brand')], max_length=100),
        ),
    ]