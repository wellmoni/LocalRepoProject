from django.shortcuts import render
from rest_framework import generics
from .models import MyModel
from my_app.serializers import MyModelSerializer
from my_app.models import Book
from my_app.models import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# Create your views here.
