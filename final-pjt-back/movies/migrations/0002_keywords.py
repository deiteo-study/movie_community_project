# Generated by Django 3.2.12 on 2023-05-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_words', models.TextField()),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
