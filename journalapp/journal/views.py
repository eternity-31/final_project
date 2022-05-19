from django.shortcuts import render
from django.urls import reverse

from .models import Journal
from django.views.generic import ListView, UpdateView, CreateView, DetailView

# Create your views here.
from .forms import JournalForm
class JournalListView(ListView):
    model = Journal
    template_name = "journal_list.html"
    context_object_name = "journal_list"

class JournalListCreate(CreateView):
    model = Journal
    template_name = "journal_create.html"
    form_class = JournalForm
    def get_success_url(self):
        return reverse('list')

class Journallistdetail(DetailView):
      model = Journal
      template_name = 'journal_detail.html'
