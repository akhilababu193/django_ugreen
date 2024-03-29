# Generated by Django 3.2.7 on 2021-09-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urbangreen', '0003_auto_20210908_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='ug_blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('desc', models.TextField()),
                ('heading', models.TextField()),
            ],
        ),
    ]
