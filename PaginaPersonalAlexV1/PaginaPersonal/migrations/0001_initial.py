# Generated by Django 2.1.7 on 2019-11-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conexiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroConexiones', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('ip', models.TextField(max_length=100)),
                ('pais', models.TextField(max_length=100)),
                ('ciudad', models.TextField(max_length=100)),
                ('postcode', models.TextField(max_length=100)),
                ('coordenadas', models.TextField(max_length=100)),
            ],
        ),
    ]
