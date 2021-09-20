
from rest_framework import serializers
from apps.post.models import Post


class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		exclude = ('deleted_at', )
		depth = 0