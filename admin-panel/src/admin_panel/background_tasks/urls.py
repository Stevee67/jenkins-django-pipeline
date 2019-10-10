from django.conf.urls import url
from .views import RunSanicBackground


urlpatterns = [
    url('sanic/', RunSanicBackground.as_view(), name='sanic-background'),
]
