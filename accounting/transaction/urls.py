from django.urls import path
from . import views
from django.conf.urls import url


app_name='transaction'

urlpatterns = [
    url('index', views.TransactionView.as_view(), name='post'),

]
