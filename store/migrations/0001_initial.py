# Generated by Django 3.0.6 on 2020-05-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
