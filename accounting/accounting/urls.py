from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

import transaction.views as transaction_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('transaction.urls')),
]
