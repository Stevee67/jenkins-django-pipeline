from django.shortcuts import HttpResponse
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView


class HealthCheck(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('IT IS OK')


class SAPView(ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse('IT IS OK')

    def get(self, request, *args, **kwargs):
        return HttpResponse('IT IS OK')
