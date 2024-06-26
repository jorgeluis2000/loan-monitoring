# Generated by Django 5.0.6 on 2024-06-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_paymentdetail_loan_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentByCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=60, unique=True)),
                ('customer_external_id', models.CharField(max_length=60, unique=True)),
                ('loan_external_id', models.CharField(max_length=60, unique=True)),
                ('payment_date', models.DateTimeField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Completado'), (2, 'Rechazado')], default=1)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('payment_amount', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
