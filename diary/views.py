from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary


class DiaryCreateView(CreateView):
    model = Diary
    fields = '__all__'
    template_name = 'diary/diary_create.html'
    success_url = reverse_lazy('diary:list')


class DiaryDetailView(DetailView):
    model = Diary


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('diary:list')


def diary_delete(request, pk):
    diary = Diary.objects.get(id=pk)
    diary.delete()

    return redirect('diary:list')