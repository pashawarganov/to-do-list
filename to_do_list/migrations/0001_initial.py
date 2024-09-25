# Generated by Django 5.1.1 on 2024-09-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('deadline_date_time', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tasks', to='to_do_list.tag')),
            ],
            options={
                'ordering': ['done', '-date_time'],
            },
        ),
    ]
