
import jwt
from rest_framework import permissions

from datetime import datetime


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
    	try:
    		user_id = request.session['user_id']
    		cur_date = datetime.now()

    		# request.heade

    		if user_id:
				payload = jwt.decode(token, "i dont know", algorithms="HS256")

				expire_at = payload.get('expire_at', None)

				# if expire_at:
    			return True
    		else:
    			return False

    	except Exception :
    		return False