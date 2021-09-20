from django.contrib import admin
from apps.post.models import Post, UserActivity

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'user_id', 'created_at')
	exclude = ('deleted_at', )


class UserActivityAdmin(admin.ModelAdmin):
	list_display = ('post_id', 'user_id', 'created_at', 'like')
	exclude = ('deleted_at', )


admin.site.register(Post, PostAdmin)

admin.site.register(UserActivity, UserActivityAdmin)
