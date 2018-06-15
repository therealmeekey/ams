# Generated by Django 2.0.6 on 2018-06-15 01:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'ЦИК'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name_plural': 'Исполнители',
                'verbose_name': 'Исполнитель',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание проблемы')),
                ('cabinet', models.CharField(max_length=5, verbose_name='Кабинет')),
                ('published_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата')),
                ('status', models.CharField(choices=[('In the work', 'В работе'), ('New', 'Новая'), ('Complited', 'Завершена')], default='New', max_length=15, verbose_name='Статус')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='Телефон')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
                'permissions': (('can_add_change', 'Пользователь'), ('can_close', 'Техническая поддержка')),
            },
        ),
        migrations.AddField(
            model_name='executor',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_executor', to='helpdesk.Ticket', verbose_name='Заявка'),
        ),
    ]
