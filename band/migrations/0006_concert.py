# Generated by Django 5.1.1 on 2024-09-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0005_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='concert_images/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('link', models.URLField(verbose_name='Ссылка на мероприятие')),
            ],
            options={
                'verbose_name': 'Концерт',
                'verbose_name_plural': 'Концерты',
            },
        ),
    ]
