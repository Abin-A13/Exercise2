from datetime import datetime
from .models import User
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets,status
from rest_framework.views import APIView
import jwt



class UserView(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is  None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            "id" : user.id,
            "iat" :datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        return Response({"token":token},status=status.HTTP_200_OK)


