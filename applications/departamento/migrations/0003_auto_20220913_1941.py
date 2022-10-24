# Generated by Django 3.2 on 2022-09-13 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
