# Generated by Django 4.1.7 on 2023-05-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_thetask_taskpriority_delete_weeklytodolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='thetask',
            name='suggesteddeadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
