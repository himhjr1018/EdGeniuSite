# Generated by Django 4.2.1 on 2023-07-22 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EdGeniusApp', '0002_instructor_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='is_instructor',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_student',
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor')], default='Student', max_length=10),
        ),
    ]