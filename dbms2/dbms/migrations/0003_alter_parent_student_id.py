# Generated by Django 4.0.2 on 2022-04-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0002_grade_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
