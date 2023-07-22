# Generated by Django 4.1.7 on 2023-05-01 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_assessment'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyTodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start_date', models.DateField(blank=True, null=True)),
                ('week_end_date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('accomplished', models.BooleanField(default=False)),
                ('crtd', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
