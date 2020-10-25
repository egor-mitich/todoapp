# Generated by Django 2.1.5 on 2020-10-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('is_completed', models.BooleanField(default=False, verbose_name='выполнено')),
            ],
        ),
    ]
