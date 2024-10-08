# Generated by Django 5.1.1 on 2024-09-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0003_alter_video_youtube_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='Фото')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['order'],
            },
        ),
    ]
