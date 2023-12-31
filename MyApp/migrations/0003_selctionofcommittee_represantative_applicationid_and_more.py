# Generated by Django 4.2.4 on 2023-08-08 11:24

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_represantative'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='represantative',
            name='ApplicationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.application'),
        ),
        migrations.CreateModel(
            name='TeamOfficials',
            fields=[
                ('TeamOfficialId', models.AutoField(primary_key=True, serialize=False)),
                ('TeamOffName', models.CharField(max_length=255)),
                ('TeamOffSurname', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Designation', models.CharField(max_length=255)),
                ('ApplicationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.application')),
            ],
        ),
    ]
