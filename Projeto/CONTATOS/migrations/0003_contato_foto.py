# Generated by Django 3.2.9 on 2021-12-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CONTATOS', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]