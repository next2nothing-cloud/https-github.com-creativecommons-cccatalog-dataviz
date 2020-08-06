from django.urls import path
from linked_commons import views


urlpatterns = [
    path("graph-data/", views.serve_graph_data),
    path("suggestions/", views.serve_suggestions),
]
