from django.shortcuts import HttpResponse
from rest_framework.generics import CreateAPIView
from .backgrounds import SanicDemoSource


class RunSanicBackground(CreateAPIView):

    def post(self, request, *args, **kwargs):
        result = SanicDemoSource().run()
        print(result)
        return HttpResponse('IT IS OK')
