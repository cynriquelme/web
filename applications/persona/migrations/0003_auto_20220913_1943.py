# Generated by Django 3.2 on 2022-09-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20220913_1941'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Habilidad',
            new_name='Habilidades',
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
