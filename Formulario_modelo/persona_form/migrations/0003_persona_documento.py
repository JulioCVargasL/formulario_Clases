# Generated by Django 5.0.4 on 2024-04-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona_form', '0002_doc_type_persona_tipo_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='documento',
            field=models.IntegerField(null=True),
        ),
    ]
