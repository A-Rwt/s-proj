# Generated by Django 4.1.1 on 2022-09-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('p_name', models.CharField(max_length=50)),
                ('p_description', models.CharField(max_length=50)),
                ('p_price', models.IntegerField()),
                ('p_discount', models.IntegerField(default=0)),
            ],
        ),
    ]
