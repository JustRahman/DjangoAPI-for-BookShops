# Generated by Django 4.2 on 2023-05-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=2000)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
