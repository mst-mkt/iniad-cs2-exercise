from django.contrib import admin
from django.urls import path

import app01.views
import forecast.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("top/", app01.views.root),
    path("", app01.views.root, name="root"),
    path("app01/pattern/<username>/", app01.views.pattern, name="pattern"),
    path("app01/param/", app01.views.param, name="param"),
    path("forecast/", forecast.views.index, name="forecast"),
]
