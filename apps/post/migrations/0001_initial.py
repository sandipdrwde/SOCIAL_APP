# Generated by Django 3.0.6 on 2021-09-20 10:44

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
            name='Post',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=50)),
                ('like', models.BooleanField(db_column='Like', default=False)),
                ('description', models.CharField(db_column='Description', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='UpdatedAt')),
                ('deleted_at', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('user_id', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Post',
                'ordering': ('created_at',),
                'managed': True,
            },
        ),
    ]
