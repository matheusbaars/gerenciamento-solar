# Generated by Django 3.0.3 on 2020-05-18 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=40)),
                ('temperatura_janeiro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_fevereiro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_marco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_abril', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_maio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_junho', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_julho', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_agosto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_setembro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_outubro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_novembro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_dezembro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temperatura_media', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
