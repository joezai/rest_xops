# Generated by Django 2.1.7 on 2020-04-26 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modellog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logsentry',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='对象'),
        ),
    ]
