# Generated by Django 4.1.7 on 2023-03-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startAdd', models.TextField()),
                ('startNick', models.CharField(max_length=500)),
                ('targetAdd', models.TextField()),
                ('targetNick', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]