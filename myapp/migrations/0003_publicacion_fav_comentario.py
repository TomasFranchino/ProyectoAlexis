# Generated by Django 4.2.5 on 2023-09-19 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_publicacion_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='fav',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.publicacion')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='myapp.publicacion')),
            ],
            bases=('myapp.publicacion',),
        ),
    ]