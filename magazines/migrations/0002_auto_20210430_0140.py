# Generated by Django 3.1.4 on 2021-04-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subarticle',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
