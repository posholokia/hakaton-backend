# Generated by Django 5.0.6 on 2024-06-16 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0009_brand_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avgbill',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='collaborationinterest',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='format',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='presencetype',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='readinesspublicspeaker',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='subscount',
            old_name='name',
            new_name='text',
        ),
    ]