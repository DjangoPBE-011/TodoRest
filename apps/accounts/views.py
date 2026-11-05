
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.authtoken.models import Token

from .serializers import RegisterUserSerializer

# Create your views here.



class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer




# token auth

# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, username=email, password=password)
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response({'error': 'Invalid credentials'}, status=400)


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         user.auth_token.delete()
#         return Response({'message': 'Logged out successfully'})









#session auth 


# class RegisterUser(CreateAPIView):
#     # serializer_class = RegisterUserSerializer
#     serializer_class = RegisterUserSerializer  # kelgan ma'lumotni tekshiradi va yangi foydalanuvchini yaratadi
#     authentication_classes = []  # session/CSRF tekshiruvini o'chiradi, shuning uchun 403 CSRF xatosi chiqmaydi kim kira oladi 
#     permission_classes = [AllowAny]  # login qilmagan hamma foydalanuvchi bu endpointga kira oladi ruxsati bormi yoqmi
    
#     def get(self, request, *args, **kwargs):
#         self.seriallizer_class = RegisterUserSerializer
#         return Response({"message": "This is a GET request"}, status=status.HTTP_200_OK)
    
    
# class Login(APIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]


#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         user = authenticate(request,email=email, password=password)
        
#         if user is not None:
#             login(request,user)
#             return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        
# class Logout(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         # 1. So'rov yuborgan foydalanuvchini aniqlaymiz va sessiyani tozalaymiz
#         user = request.user

#         # logout() sessiyani o'zi ham tozalaydi (flush qiladi)
#         logout(request)

#         # 2. Brauzer kukilarini tozalash uchun javob tayyorlaymiz
#         response = Response(
#             {'message': f'User {user.email} logged out successfully'},
#             status=status.HTTP_200_OK,
#         )

#         # Kuki nomlarini sozlamalardan olib o'chiramiz
#         response.delete_cookie(settings.SESSION_COOKIE_NAME)
#         response.delete_cookie(settings.CSRF_COOKIE_NAME)

#         return response
    
    
    

    
    
    
    
    
    
    

    

# class ExampleView(APIView):
#     def get(self, request, *args, **kwargs):
        
#         print(request)
        
#         query_params = request.query_params
#         print(query_params,"################")
        
#         name = query_params.get('name')
#         fullname = query_params.get('fullname')

#         print(name,fullname,"################")
        
#         return Response({"message": query_params}, status=status.HTTP_200_OK)


# class Example2View(APIView):
    
#     def get(self, request, *args, **kwargs):
        
#         path_args = kwargs.get('pk')
#         print(path_args,"################")
        
#         header = request.headers
#         print(header,"################")
        
#         body = request.data
#         print(body,"################")
        
#         return Response({'message': path_args, 'headers': header, 'body': body}, status=status.HTTP_200_OK)
