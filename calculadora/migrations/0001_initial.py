# Generated by Django 3.0.3 on 2020-05-03 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipamentos', '0002_modulo_fotovoltaico_tier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teste', models.CharField(blank=True, max_length=10, null=True)),
                ('irradiacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.Irradiacao')),
            ],
        ),
    ]
