# JournalListView(ListView)
from django.urls import path

from . import views
urlpatterns = [
    path('', views.JournalListView.as_view(), name='list'),
    path('create/', views.JournalListCreate.as_view(), name='create'),
    path('<int:pk>', views.Journallistdetail.as_view(), name='detail')]