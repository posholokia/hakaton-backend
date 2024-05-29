# Generated by Django 5.0.6 on 2024-05-29 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Formats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название формата')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
            },
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название цели')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('fi', models.CharField(max_length=128, verbose_name='Фамилия и имя')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('tg_nickname', models.CharField(max_length=128, verbose_name='Ник в телеграме')),
                ('brand_name_pos', models.CharField(max_length=128, verbose_name='Название бренда и должность')),
                ('inst_brand_url', models.URLField(verbose_name='Бренд в Instagram')),
                ('inst_profile_url', models.URLField(verbose_name='Профиль в Instagram')),
                ('tg_brand_url', models.URLField(verbose_name='Telegram-канал')),
                ('brand_site_url', models.URLField(verbose_name='Сайт бренда')),
                ('topics', models.TextField(verbose_name='Темы')),
                ('subs_count', models.CharField(choices=[('1k', '0 - 1000'), ('10k', '1000 - 10000'), ('100K', '10000 - 100000'), ('500k', '100000 - 500000'), ('INF', '500000+')], max_length=4, verbose_name='Кол-во подписчиков в Instagram')),
                ('avg_bill', models.CharField(choices=[('1k', '0 - 1000'), ('10k', '1000 - 10000'), ('100K', '10000 - 100000'), ('500k', '100000 - 500000'), ('INF', '500000+')], max_length=4, verbose_name='Средний чек')),
                ('values', models.CharField(max_length=255, verbose_name='Ценности')),
                ('target_audience', models.TextField(verbose_name='Целевая аудитория')),
                ('territory', models.CharField(max_length=128, verbose_name='География бренда')),
                ('logo', models.ImageField(upload_to='logos', verbose_name='Лого')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Фото представителя')),
                ('product_photo', models.ImageField(upload_to='product_photos', verbose_name='Фото продукта')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('business_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to='brand.category', verbose_name='Категория')),
                ('collab_with', models.ManyToManyField(related_name='brand_collab_with', to='brand.category', verbose_name='Категории коллаборации')),
                ('formats', models.ManyToManyField(related_name='brands', to='brand.formats', verbose_name='Форматы')),
                ('goal', models.ManyToManyField(related_name='brands', to='brand.goals', verbose_name='Цель')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
    ]