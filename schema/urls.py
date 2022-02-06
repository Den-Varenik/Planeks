from django.urls import path

from schema import views

urlpatterns = [
    path('', views.SchemasListView.as_view(), name="schema-list"),
    path('create/', views.SchemaCreateView.as_view(), name="schema-create"),
]
