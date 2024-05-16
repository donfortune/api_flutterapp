from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes),
    path('note/<int:id>/', views.getNote),
    path('notes/create/', views.createNote),
    path('notes/<int:id>/update', views.updateNote),
    path('notes/<int:id>/delete', views.deleteNote)
    ]