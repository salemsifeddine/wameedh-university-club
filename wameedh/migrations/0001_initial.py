# Generated by Django 3.2.8 on 2021-10-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='aboutImages')),
            ],
        ),
        migrations.CreateModel(
            name='ClubAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='clubAchivemetns')),
            ],
        ),
        migrations.CreateModel(
            name='ClubEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='clubEvents')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(null=True, upload_to='members_images')),
            ],
        ),
    ]
