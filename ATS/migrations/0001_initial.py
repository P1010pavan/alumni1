# Generated by Django 3.2 on 2021-07-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=200)),
                ('Date', models.DateField(auto_now=True)),
                ('Description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=200)),
                ('Date', models.DateField(auto_now=True)),
                ('Description', models.TextField(null=True)),
                ('Image', models.ImageField(default='', upload_to='story/')),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]
