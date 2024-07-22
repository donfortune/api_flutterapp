from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes),
    path('note/<int:id>/', views.getNote),
    path('notes/create/', views.createNote),
    path('notes/<int:id>/update', views.updateNote),
    path('notes/<int:id>/delete', views.deleteNote)
    ]