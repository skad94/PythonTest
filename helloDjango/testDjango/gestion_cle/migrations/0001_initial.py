# Generated by Django 4.1 on 2024-10-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('identificat', models.IntegerField()),
                ('equipe', models.CharField(choices=[('CA', "Conseil d'Administration"), ('SONO', 'Musique et son'), ('ext', ' exterieures ou autres')], default='ext', max_length=50)),
            ],
        ),
    ]
