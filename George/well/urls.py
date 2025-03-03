from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("books/", include("well.urls")),  # Maps the "books/" URL to book_store app
    path("admin/", admin.site.urls),
]
