# Generated by Django 3.2.10 on 2022-08-11 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_service', '0002_auto_20220811_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyresource',
            name='student',
        ),
        migrations.AlterField(
            model_name='revisionclass',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revision_class_subject', to='custom_service.subject'),
        ),
    ]
