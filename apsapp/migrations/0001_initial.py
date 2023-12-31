# Generated by Django 4.1.7 on 2023-05-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], max_length=10)),
                ('dateofbirth', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField(unique=True)),
                ('registrationtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'customer_table',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'feedback_table',
            },
        ),
        migrations.CreateModel(
            name='Zodiacsign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Adult', 'Adult'), ('Child', 'Child'), ('Parent', 'parent')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('image', models.FileField(upload_to='zodiacimages')),
            ],
            options={
                'db_table': 'zodiac_table',
            },
        ),
    ]
