# Generated by Django 2.0 on 2022-06-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220630_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetssubcategory',
            name='subcat_image',
            field=models.FileField(default='Assetmgtsysimg.png', upload_to='images/'),
        ),
    ]
