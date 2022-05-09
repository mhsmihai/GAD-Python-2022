# Generated by Django 4.0.4 on 2022-05-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=11)),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('how_to_apply', models.TextField(max_length=150)),
            ],
        ),
    ]
