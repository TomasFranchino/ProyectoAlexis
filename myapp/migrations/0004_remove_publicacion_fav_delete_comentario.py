# Generated by Django 4.2.5 on 2023-09-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_publicacion_fav_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='fav',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]