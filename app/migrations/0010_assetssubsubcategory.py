# Generated by Django 2.0 on 2011-11-08 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220630_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsSubsubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subsubcat_Title', models.CharField(max_length=50)),
                ('subsubcat_image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('AssetsSubCategoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AssetssubCategory')),
            ],
        ),
    ]
