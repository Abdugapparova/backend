# Generated by Django 4.2 on 2023-04-26 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('rating', models.FloatField()),
                ('price', models.FloatField()),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genres')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Movies_viewed',
            fields=[
                ('viewed_movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movies')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Movies_saved',
            fields=[
                ('saved_movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movies')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
    ]
