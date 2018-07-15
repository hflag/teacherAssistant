# Generated by Django 2.0.6 on 2018-07-12 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_auto_20180711_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='act',
            name='score',
        ),
        migrations.RemoveField(
            model_name='act',
            name='student',
        ),
        migrations.AddField(
            model_name='studentactscore',
            name='act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Act'),
        ),
        migrations.AddField(
            model_name='studentactscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Student'),
        ),
    ]