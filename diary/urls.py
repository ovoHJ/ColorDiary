from django.urls import path

from diary.views import DiaryListView

app_name = 'diary'

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
]