# Generated by Django 4.2.14 on 2024-09-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacher_tsc_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tsc_number',
            field=models.CharField(default='DEFAULT_TSC_NUMBER', max_length=100),
        ),
    ]
