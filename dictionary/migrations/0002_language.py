# Generated by Django 2.2 on 2019-04-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialect', models.CharField(max_length=50)),
                ('word', models.CharField(max_length=50)),
            ],
        ),
    ]