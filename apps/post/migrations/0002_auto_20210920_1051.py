# Generated by Django 3.0.6 on 2021-09-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(db_column='Id', max_length=10, primary_key=True, serialize=False),
        ),
    ]