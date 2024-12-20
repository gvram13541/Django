### {{ *** }} GENERIC CLASS BASED VIEWS {{ *** }} ###

from django.contrib.auth.models import User
from Users.serializers import CreateUserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class UsersListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    
    
class UserDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer








### {{ *** }} CLASS BASED VIEWS WITH Mixins {{ *** }} ###

# from django.contrib.auth.models import User
# from Users.serializers import CreateUserSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class UsersListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class UserDetailsView(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)











### {{ *** }} CLASS BASED VIEWS {{ *** }} ###

# from django.contrib.auth.models import User
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from Users.serializers import CreateUserSerializer


# class UsersListView(APIView):
#     """
#     List all the Users or Create a new User
    
#     """
    
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = CreateUserSerializer(users, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = CreateUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class UserDetailsView(APIView):
#     """
#     Retrieve, Update or Delete a User instance
    
#     """
    
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Http404
        
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = CreateUserSerializer(user)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = CreateUserSerializer(user)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)









### {{ *** }} FUNCTION BASED VIEWS {{ *** }} ###

# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from Users.serializers import CreateUserSerializer


# @api_view(['GET','POST'])
# def ListAllUsers(request, format=None):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = CreateUserSerializer(users, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = CreateUserSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def UserView(request, pk, format=None):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = CreateUserSerializer(user)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = CreateUserSerializer(user, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        