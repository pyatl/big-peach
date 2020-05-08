# Generated by Django 3.0.2 on 2020-02-04 03:55

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('map_embed_code', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('short_description', models.TextField(max_length=280)),
                ('description', tinymce.models.HTMLField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('published', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.Location')),
            ],
            options={
                'ordering': ['start'],
            },
        ),
    ]
