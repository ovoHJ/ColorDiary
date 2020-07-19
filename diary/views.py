from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary


class DiaryCreateView(CreateView):
    model = Diary
    fields = '__all__'
    template_name = 'diary/diary_create.html'
    success_url = reverse_lazy('diary:list')


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('diary:list')


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:list')
