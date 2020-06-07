# Generated by Django 3.0.3 on 2020-05-18 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_modulo_fotovoltaico_tier'),
        ('orcamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='inversor_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipamentos.Inversor_fotovoltaico'),
        ),
    ]
