# Generated by Django 3.1 on 2022-07-10 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0007_place_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='NoCategory', max_length=200)),
            ],
        ),
    ]
