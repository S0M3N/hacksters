# Generated by Django 4.0.6 on 2022-09-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=10)),
                ('branch', models.CharField(blank=True, max_length=70, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
