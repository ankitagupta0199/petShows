# Generated by Django 2.1.5 on 2019-04-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addpost',
            fields=[
                ('adsid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('adstitle', models.CharField(max_length=100)),
                ('adssubcat', models.CharField(max_length=50)),
                ('adsdescription', models.CharField(max_length=100)),
                ('adsprice', models.CharField(max_length=100)),
                ('file1', models.CharField(max_length=100)),
                ('file2', models.CharField(max_length=100)),
                ('file3', models.CharField(max_length=100)),
                ('file4', models.CharField(max_length=100)),
                ('adscity', models.CharField(max_length=50)),
                ('bstatus', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]