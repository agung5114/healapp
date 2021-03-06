# Generated by Django 3.2.7 on 2021-09-16 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('menu', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('kkal', models.IntegerField()),
                ('lemak', models.IntegerField()),
                ('karbohidrat', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('risiko', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=128)),
                ('umur', models.IntegerField()),
                ('bb', models.IntegerField()),
                ('tb', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('penyakit', models.CharField(max_length=40)),
                ('diabetes', models.BooleanField()),
                ('jantung', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Minum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_minum', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Makan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('menu_makan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.makanan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
