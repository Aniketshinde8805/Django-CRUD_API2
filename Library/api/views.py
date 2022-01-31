from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BookSerializer
from .models import Book
from rest_framework import status
# Create your views here.

class BookList(APIView):
	

	def get(self,request):
		book=Book.objects.all()
		serializer=BookSerializer(book,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer=BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class BookDetail(APIView):
	def get(self,request,id):
		book=Book.objects.get(pk=id)
		serializer=BookSerializer(book)
		return Response(serializer.data)

	def delete(self,request,id):
		book=Book.objects.get(pk=id)
		book.delete()
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,id):
		book=Book.objects.get(pk=id)
		serializer=BookSerializer(book,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,id):
		book=Book.objects.get(pk=id)
		serializer=BookSerializer(book,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 
  