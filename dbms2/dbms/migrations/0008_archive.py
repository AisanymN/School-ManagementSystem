# Generated by Django 4.0.2 on 2022-04-28 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0007_remove_grade_student_id_remove_grade_subject_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms.student')),
            ],
        ),
    ]
