# Generated by Django 3.2.7 on 2022-02-03 16:51

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('car_type', models.CharField(choices=[('SD', 'Sedan'), ('SR', 'Sports'), ('SUV', 'Suv')], default='SD', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=30)),
                ('club_ranking', models.CharField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], default=4, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('media_type', models.CharField(choices=[('Audio', (('Cd', 'Cd'), ('Cas', 'Cassette'))), ('Video', (('VHS', 'VHS Tape'), ('DVD', 'DVD'))), ('Unknown', 'Unknown')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ModelFieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_integer', models.BigIntegerField()),
                ('boolean', models.BooleanField()),
                ('binary', models.BinaryField()),
                ('full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('username', models.CharField(error_messages={'blank': 'Enter a username'}, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField()),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration', models.DurationField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('num', models.FloatField()),
                ('upload_file', models.FileField(upload_to=None)),
                ('image', models.ImageField(upload_to=None)),
                ('integer', models.IntegerField()),
                ('positive_integer', models.PositiveIntegerField()),
                ('positive_big_integer', models.PositiveBigIntegerField()),
                ('positive_small_integer', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('small_integer', models.SmallIntegerField()),
                ('text', models.TextField()),
                ('time', models.TimeField()),
                ('url', models.URLField()),
                ('uuid', models.UUIDField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='MoonLanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('astranaut_name', models.CharField(blank=True, max_length=100)),
                ('moon_landings', models.DateField(choices=[(datetime.date(1969, 7, 20), 'Apollo 11 (Eagle)'), (datetime.date(1969, 11, 19), 'Apollo 12 (Intrepid)'), (datetime.date(1971, 2, 5), 'Apollo 14 (Antares)'), (datetime.date(1971, 7, 30), 'Apollo 15 (Falcon)'), (datetime.date(1972, 4, 21), 'Apollo 16 (Orion)'), (datetime.date(1972, 12, 11), 'Apollo 17 (Challenger)')])),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('H', 'Horror'), ('S', 'Science Fiction'), ('R', 'Romance'), ('A', 'Action'), ('U', 'Unknown')], default='U', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=15)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ValidatorPracticeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabet are allowed.')])),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Only alphanumeric characters and @ ! are allowed.', regex='^[0-9a-zA-Z@!]*$')])),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=100, message='Your value should be greater than hundred')])),
                ('max_amount', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=1000000, message='Your amount cannot be greater than ten lakhs')])),
                ('code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='Your code must be atleast 4 character long.')])),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
