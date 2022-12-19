# Generated by Django 4.1.3 on 2022-12-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_remove_pedidoservicio_duracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoservicio',
            name='estado',
            field=models.CharField(choices=[('En espera', 'En espera'), ('Realizar Primer Pago', 'Realizar Primer Pago'), ('Pagado Primer Pago', 'Pagado Primer Pago'), ('Realizar Segundo Pago', 'Realizar Segundo Pago'), ('Pagado Segundo Pago', 'Pagado Segundo Pago'), ('Finalizado', 'Finalizado')], default='En espera', max_length=100),
        ),
    ]
