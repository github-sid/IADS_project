# Generated by Django 4.2.5 on 2023-11-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('current_price_cad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('current_price_eur', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('market_cap', models.IntegerField()),
                ('market_cap_rank', models.PositiveIntegerField()),
                ('fully_diluted_valuation', models.IntegerField(blank=True, null=True)),
                ('total_volume', models.IntegerField(blank=True, null=True)),
                ('high_24h', models.IntegerField(blank=True, null=True)),
                ('low_24h', models.IntegerField(blank=True, null=True)),
                ('price_change_24h', models.IntegerField(blank=True, null=True)),
                ('price_change_percentage_24h', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('market_cap_change_24h', models.IntegerField(blank=True, null=True)),
                ('market_cap_change_percentage_24h', models.IntegerField(blank=True, null=True)),
                ('circulating_supply', models.IntegerField(blank=True, null=True)),
                ('total_supply', models.IntegerField(blank=True, null=True)),
                ('max_supply', models.IntegerField(blank=True, null=True)),
                ('ath', models.IntegerField(blank=True, null=True)),
                ('ath_change_percentage', models.IntegerField(blank=True, null=True)),
                ('ath_date', models.DateTimeField(blank=True, null=True)),
                ('atl', models.IntegerField(blank=True, null=True)),
                ('atl_change_percentage', models.IntegerField(blank=True, null=True)),
                ('atl_date', models.DateTimeField(blank=True, null=True)),
                ('roi', models.FloatField(null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
