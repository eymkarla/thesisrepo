# Generated by Django 2.2 on 2019-04-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialect', models.CharField(max_length=50)),
                ('word', models.CharField(max_length=50)),
                ('meaning', models.TextField()),
            ],
        ),
    ]
