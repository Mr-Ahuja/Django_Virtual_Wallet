# Generated by Django 2.2.5 on 2019-10-30 22:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('routing_number', models.IntegerField(validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)])),
                ('account_number', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_type', models.CharField(max_length=45)),
                ('card_number', models.IntegerField(validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MaxLengthValidator(16)])),
                ('owner_first_name', models.CharField(max_length=45)),
                ('owner_last_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='account_owner', to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('amount', models.FloatField(default=0.0)),
                ('description', models.CharField(max_length=200)),
                ('recipients', models.CharField(max_length=45)),
                ('payment_type', models.CharField(max_length=45)),
                ('is_complete', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='banks', to='app.Bank')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cards', to='app.Card')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wallet', to='app.Wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('friendship_id', models.AutoField(primary_key=True, serialize=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friendship_creator', to='app.User')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend', to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='card_owner', to='app.User'),
        ),
        migrations.AddField(
            model_name='bank',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bank_owner', to='app.User'),
        ),
    ]