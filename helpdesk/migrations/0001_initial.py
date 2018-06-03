# Generated by Django 2.0.6 on 2018-06-03 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание проблемы')),
                ('cabinet', models.CharField(max_length=5, verbose_name='Кабинет')),
                ('published_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата')),
                ('status', models.CharField(choices=[('In the work', 'В работе'), ('New', 'Новая'), ('Complited', 'Завершена')], default='New', max_length=15, verbose_name='Статус')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='Телефон')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'permissions': (('can_add_change', 'Пользователь'), ('can_close', 'Техническая поддержка')),
            },
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_executor', to='helpdesk.Application', verbose_name='Заявка')),
                ('owner', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'ЦИК'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
    ]