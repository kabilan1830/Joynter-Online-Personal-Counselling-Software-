# Generated by Django 3.2.4 on 2021-06-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_unisignin'),
    ]

    operations = [
        migrations.CreateModel(
            name='stdregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('ename', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('add', models.CharField(max_length=100)),
                ('pschool', models.CharField(max_length=100)),
                ('school_add', models.CharField(max_length=100)),
                ('school_doc', models.CharField(max_length=100)),
                ('LDA', models.CharField(max_length=100)),
            ],
        ),
    ]
