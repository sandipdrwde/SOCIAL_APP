
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.post.models import Post
from apps.post.serializers import PostSerializer 

from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.


@permission_classes((IsAuthenticated, ))

class PostView(APIView):
	def get(self, request):
		try:
			# params = request.query_params
			# print(params)
			posts = Post.objects.all()
			posts = PostSerializer(posts, many=True).data

			return Response({'response':posts}, status=status.HTTP_200_OK)
		except Exception as err:
			return Response({"error":str(err)}, status=status.HTTP_400_BAD_REQUEST)


	def post(self, request):
		try:
			params = request.data

			user_id = request.session['user_id']


			user_id = User.objects.get(id=user_id)



			posts = Post.objects.create(
				title = params['title'],
				description = params['description'],
				user_id = user_id,
			)

			posts = PostSerializer(posts).data
			return Response({'response':posts}, status=status.HTTP_200_OK)
		except Exception as err:
			return Response({"error":str(err)}, status=status.HTTP_400_BAD_REQUEST)


