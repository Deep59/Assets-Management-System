# Generated by Django 2.0 on 2011-11-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_assets_assetssubsubcategory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetssubcategory',
            name='subcat_image',
        ),
        migrations.RemoveField(
            model_name='assetssubsubcategory',
            name='subsubcat_image',
        ),
    ]