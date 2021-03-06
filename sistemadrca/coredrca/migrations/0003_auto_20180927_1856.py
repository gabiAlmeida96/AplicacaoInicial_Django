# Generated by Django 2.1.1 on 2018-09-27 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coredrca', '0002_aluno_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='credito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coredrca.Credito'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, to='coredrca.Disciplina'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='d_requisito',
            field=models.ManyToManyField(blank=True, to='coredrca.Disciplina'),
        ),
    ]
