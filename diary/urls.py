from django.urls import path

from diary.views import DiaryListView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView, DiaryDetailView

app_name = 'diary'

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', DiaryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', DiaryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DiaryDeleteView.as_view(), name='delete'),
]