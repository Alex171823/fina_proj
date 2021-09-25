# Generated by Django 3.2.3 on 2021-09-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='/', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255),
        ),
    ]