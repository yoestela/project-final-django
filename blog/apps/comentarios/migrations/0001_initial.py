# Generated by Django 4.2.3 on 2023-07-24 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ('fecha_creacion',),
            },
        ),
    ]
