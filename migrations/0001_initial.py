# Generated by Django 2.2.5 on 2021-05-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.IntegerField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
    ]
