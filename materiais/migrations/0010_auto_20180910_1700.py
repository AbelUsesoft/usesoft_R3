# Generated by Django 2.0.2 on 2018-09-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0009_categoria_ultima_alteracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidonf',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidonfitem',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoweb',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidowebitem',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produtotributacao',
            name='ultima_alteracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
