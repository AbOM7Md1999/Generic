from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions
from django.shortcuts import render


# Create your views here.


class BookList (generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

class BookDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer



def home(request):
    return render(request,'../templates/index.html')


    



