# Generated by Django 3.0.1 on 2020-02-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcard', '0010_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentunit',
            name='student_unit',
            field=models.CharField(max_length=191),
        ),
    ]