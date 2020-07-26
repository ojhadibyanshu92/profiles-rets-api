from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello_view/',views.HelloAPIView.as_view()),
]