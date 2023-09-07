from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )

        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})

class NewsApiView(APIView):
    serializer_class = NewsSerializer
    def get(self,request):
        allNews=News.objects.all().values()
        return Response({"Message":"List of News", "News List":allNews})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=NewsSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            News.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            description=serializer_obj.data.get("description"),
                            content=serializer_obj.data.get("content"),
                            
                            )

        news=News.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":news})


class PersonView(APIView):
    serializer_class = PersonSerializer
    def get(self,request):
        allNews=Person.objects.all().values()
        return Response({"Message":"List of Users", "Users List":allNews})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=PersonSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Person.objects.create(id=serializer_obj.data.get("id"),
                            name=serializer_obj.data.get("name"),
                            age=serializer_obj.data.get("age"),
                            email=serializer_obj.data.get("email"),
                            password=serializer_obj.data.get("password"),
                            
                            )

        news=Person.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New User Added!", "User":news})

