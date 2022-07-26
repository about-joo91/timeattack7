# Generated by Django 4.0.6 on 2022-07-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_jobpoststatus_jobpostactivity_job_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RecruitActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post_activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.jobpostactivity')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.recruitstatus')),
            ],
        ),
    ]
