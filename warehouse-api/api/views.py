from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response

from .models import Book, Author, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, GetRequestSerializer


class BookModelApi(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @action(methods=['POST'], detail=True)
    # def delete_book(self, request):
    #     request = request.json()
    #     queryset = Book.objects.filter(name=request['name'])
    #
    #     queryset[0].delete()
    #
    #     print(f'Book {request["name"]} done')


class AuthorModelApi(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherModelApi(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


@api_view(['POST'])
def get_request(request):
    data = JSONParser().parse(request)
    serializer = GetRequestSerializer(data=data)
    if serializer.is_valid():
        Book.objects.get(name=serializer.data['name']).delete()
        print('deleted')
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
