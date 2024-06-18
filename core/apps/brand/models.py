from typing import Type

from django.conf import settings
from django.db import models

from core.apps.chat.models import Room
from core.apps.payments.models import Subscription
from core.apps.questionnaire.models import Question


class Brand(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    published = models.BooleanField(
        default=False, verbose_name='Опубликовано'
    )
    subscription = models.ForeignKey(
        to=Subscription,
        on_delete=models.PROTECT,
        related_name='brands',
        verbose_name='Тариф',
        null=True
    )
    sub_expire = models.DateField("Окончание подписки", null=True)
    tg_nickname = models.CharField('Ник в телеграме', max_length=64)
    phone = models.CharField('Номер телефона', max_length=12)
    brand_name_pos = models.CharField(
        'Название бренда и должность',
        max_length=512
    )
    inst_brand_url = models.CharField('Бренд в Instagram', max_length=512)
    brand_site_url = models.CharField('Сайт бренда', max_length=512)
    topics = models.CharField('Темы', max_length=512)
    mission_statement = models.CharField('Миссия бренда', max_length=512)
    target_audience = models.CharField(
        'Целевая аудитория', max_length=512
    )
    unique_product_is = models.CharField(
        'Уникальность продукта', max_length=512
    )
    product_description = models.CharField(
        'Описание продукта', max_length=512
    )
    problem_solving = models.CharField(
        'Какую проблему решает', max_length=512
    )
    business_group = models.CharField(
        'Сообщество предпринимателей', max_length=512
    )
    logo = models.ImageField('Лого', upload_to='logos')
    photo = models.ImageField(
        'Фото представителя', upload_to='photos'
    )
    product_photo = models.ImageField(
        'Фото продукта', upload_to='product_photos'
    )
    fullname = models.CharField('Фамилия и имя', max_length=512)
    email = models.EmailField('Эл. почта')
    # likes = models.ManyToManyField(
    #     to='self',
    #     through='Match',
    #     through_fields=('brand1', 'brand2'),
    #     verbose_name='Лайкнул'
    # )

    def like(self, brand_pk: int):
        """
        Метод бренда, который позволяет лайкнуть другой бренд.

        Возвращает объект метча. В поле is_match которого содержится информация произошел ли метч.

        Args:
            brand_pk: первичный ключ бренда, которого нужно лайкнуть
        """
        try:
            match = Match.objects.get(initiator__pk=brand_pk, target__pk=self.pk)
        except Match.DoesNotExist:
            match = None

        if match:
            match.objects.update(is_match=True)
            has_business = any([match.initiator.has_business, match.target.has_business])
            room = Room.objects.create(has_business=has_business)
            room.participants.add(self.pk, brand_pk)
            return match
        else:
            Match.objects.create(initiator=self, target__pk=brand_pk)

        return match

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __repr__(self):
        return f'Brand name and position: {self.brand_name_pos}'


class Category(models.Model):
    brand = models.OneToOneField(
        Brand,
        on_delete=models.CASCADE,
        related_name='category',
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __repr__(self):
        return f'Category: {self.text}'


class PresenceType(models.Model):
    brand = models.OneToOneField(
        Brand,
        on_delete=models.CASCADE,
        related_name='presence_type'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Способ размещения бренда'
        verbose_name_plural = 'Способы размещения бренда'

    def __repr__(self):
        return f'PresenceType: {self.text}'


class ReadinessPublicSpeaker(models.Model):
    brand = models.OneToOneField(
        Brand,
        on_delete=models.CASCADE,
        related_name='public_speaker'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Готовность быть спикером'
        verbose_name_plural = 'Готовность быть спикером'

    def __repr__(self):
        return f'ReadinessPublicSpeaker: {self.text}'


class SubsCount(models.Model):
    brand = models.OneToOneField(
        Brand,
        on_delete=models.CASCADE,
        related_name='subs_count'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Кол-во подписчиков'
        verbose_name_plural = 'Кол-во подписчиков'

    def __repr__(self):
        return f'SubsCount: {self.text}'


class AvgBill(models.Model):
    brand = models.OneToOneField(
        Brand,
        on_delete=models.CASCADE,
        related_name='avg_bill'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Средний чек'
        verbose_name_plural = 'Средний чек'

    def __repr__(self):
        return f'AvgBill: {self.text}'


class Goal(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __repr__(self):
        return f'Goal: {self.text}'


class Format(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='formats'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Формат взаимодействия'
        verbose_name_plural = 'Форматы взаимодействия'

    def __repr__(self):
        return f'Format: {self.text}'


class CollaborationInterest(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='collaboration_interest'
    )
    text = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Интересующая коллаборация'
        verbose_name_plural = 'Интересующие коллаборации'

    def __repr__(self):
        return f'CollaborationInterest: {self.text}'


class Match(models.Model):
    initiator = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE,
        related_name='initiator',
        verbose_name='Бренд 1'
    )
    target = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE,
        related_name='target',
        verbose_name='Бренд 2'
    )
    is_match = models.BooleanField(
        default=False,
        verbose_name='Метч'
    )
