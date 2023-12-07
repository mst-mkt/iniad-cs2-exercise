from django.contrib import admin
from django.urls import path

import app01.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("top/", app01.views.root),
]
