# Generated by Django 4.1 on 2022-10-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiJuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=1)),
                ('sudoku_inicial', models.CharField(max_length=81)),
                ('sudoku_final', models.CharField(max_length=81)),
                ('numeros', models.IntegerField()),
                ('ceros', models.IntegerField()),
                ('progreso', models.FloatField(default=0)),
                ('movimientos', models.IntegerField(default=0)),
            ],
        ),
    ]