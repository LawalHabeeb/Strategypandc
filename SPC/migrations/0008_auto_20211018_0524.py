# Generated by Django 3.2.8 on 2021-10-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPC', '0007_auto_20211018_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]