# Generated by Django 4.2.7 on 2023-11-27 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finalProject_app', '0005_alter_workorders_enddate_alter_workorders_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='workOrder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='finalProject_app.workorders'),
        ),
    ]
