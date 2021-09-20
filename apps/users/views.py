
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
import jwt



class LoginView(APIView):
	def post(self, request):
		try:

			# print(dir(request))
			# import ipdb; ipdb.set_trace()
			params = request.data
			username = params['username']
			password = params['password']
			user = authenticate(username=username, password=password)

			if user:
				request.session['user_id'] = user.id
				payload = {
					'user_id':user.id,
					'expire_at':int((datetime.now() - timedelta(days=1)).timestamp())
				}
				token = jwt.encode(payload, 'i dont know', algorithm='HS256')

				resp = {
					'user_id':user.id,
					'token':token,
					'username':user.username
				}

			return Response(resp, status=status.HTTP_200_OK)

		except User.DoesNotExist:
			return Response({"error":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

		except Exception as err:
			return Response({"error":str(err)}, status=status.HTTP_400_BAD_REQUEST)
