# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_user_like_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자 목록'},
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, upload_to='user', verbose_name='프로필 이미지'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(to='post.Post', verbose_name='좋아요 누른 포스트'),
        ),
        migrations.AddField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='relations',
            field=models.ManyToManyField(through='member.Relation', to=settings.AUTH_USER_MODEL),
        ),
    ]
