# Generated by Django 2.2.6 on 2019-11-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_name', models.CharField(max_length=255)),
                ('grower', models.CharField(max_length=255)),
                ('dispensary', models.CharField(max_length=255)),
                ('cannabis', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
