# Generated by Django 4.0.2 on 2022-04-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0004_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_lname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('parent_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='parent',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_id',
        ),
    ]