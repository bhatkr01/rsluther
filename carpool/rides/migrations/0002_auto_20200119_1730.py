# Generated by Django 3.0.2 on 2020-01-19 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='username',
        ),
        migrations.AddField(
            model_name='ride',
            name='seats',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ride',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]