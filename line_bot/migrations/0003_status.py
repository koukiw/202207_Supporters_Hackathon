# Generated by Django 3.1 on 2022-07-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0002_auto_20220709_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
            ],
        ),
    ]
