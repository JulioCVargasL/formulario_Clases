# Generated by Django 5.0.4 on 2024-04-13 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='persona_form.doc_type'),
        ),
    ]