# Generated by Django 4.0.4 on 2022-05-13 22:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arma',
            name='id',
        ),
        migrations.RemoveField(
            model_name='municao',
            name='id',
        ),
        migrations.AddField(
            model_name='arma',
            name='id_arma',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='municao',
            name='id_municao',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='arma',
            name='imagem',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='arma',
            name='marca',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='arma',
            name='modelo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='municao',
            name='marca',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='municao',
            name='modelo',
            field=models.CharField(max_length=255),
        ),
    ]
