# Generated by Django 2.2.5 on 2019-12-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('coordinator', models.CharField(blank=True, max_length=200)),
                ('euc_coordinator', models.CharField(max_length=200)),
                ('euc_coordinator_email', models.EmailField(blank=True, max_length=100)),
                ('prereqs', models.CharField(blank=True, max_length=3000)),
                ('level', models.IntegerField()),
                ('quad', models.IntegerField()),
                ('blurb', models.CharField(blank=True, max_length=3000)),
                ('note', models.CharField(blank=True, max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('note', models.CharField(blank=True, max_length=3000)),
                ('courses', models.ManyToManyField(to='studytool_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_selected', models.IntegerField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=3000)),
                ('courses_mandatory', models.ManyToManyField(to='studytool_app.Course')),
                ('courses_selected', models.ManyToManyField(blank=True, null=True, related_name='selected', to='studytool_app.Course')),
            ],
        ),
    ]
