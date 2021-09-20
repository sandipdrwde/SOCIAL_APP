from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    id = models.AutoField(primary_key=True, db_column='Id')
    title = models.CharField(db_column='Title', blank=False, max_length=50)
    description = models.CharField(db_column='Description', max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='UserId')

    created_at = models.DateTimeField(auto_now_add=True, db_column='CreatedAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='UpdatedAt')
    deleted_at = models.DateTimeField(blank=True, null=True, db_column='DeletedAt')

    class Meta:
        managed = True
        db_table = 'Post'
        ordering = ('created_at',)


class UserActivity(models.Model):
    id = models.AutoField(primary_key=True, db_column ="id")
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_column='PostId')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='UserId')
    like = models.BooleanField(db_column='Like' , default=False)

    created_at = models.DateTimeField(auto_now_add=True, db_column='CreatedAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='UpdatedAt')
    deleted_at = models.DateTimeField(blank=True, null=True, db_column='DeletedAt')

    # comment =models

    class Meta:
        managed = True
        db_table = 'UserActivity'
        ordering = ('created_at',)



