# Generated by Django 4.0.5 on 2022-06-30 21:31

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorksCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'work category',
                'verbose_name_plural': 'works category',
            },
        ),
        migrations.CreateModel(
            name='WorksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('work_image', models.ImageField(upload_to='works/')),
                ('category', models.ManyToManyField(to='works.workscategorymodel')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
            },
        ),
    ]
