# Generated by Django 4.0.3 on 2022-04-12 09:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='is_admin',
            field=models.ManyToManyField(blank=True, choices=[(True, 'True'), (False, 'False')], related_name='is_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='is_member',
            field=models.ManyToManyField(blank=True, choices=[(True, 'True'), (False, 'False')], related_name='is_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='is_moderator',
            field=models.ManyToManyField(blank=True, choices=[(True, 'True'), (False, 'False')], related_name='is_moderator', to=settings.AUTH_USER_MODEL),
        ),
    ]
