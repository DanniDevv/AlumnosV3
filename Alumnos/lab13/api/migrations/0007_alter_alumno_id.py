# Generated by Django 3.2 on 2023-06-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_alumno_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
