# Generated by Django 3.2.7 on 2021-09-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=7)),
                ('user_id', models.PositiveIntegerField()),
                ('datetime', models.CharField(default='N/A', max_length=14)),
                ('score', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pics', models.ImageField(upload_to='pics')),
                ('category', models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
    ]