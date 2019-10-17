from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Material, Stock, SwitchBoard

# Create your views here.


def home(request):

    template_name = 'materials/home.html'
    context = {}
    return render(request, template_name, context)


def material(request):

    template_name = 'materials/material.html'
    context = {}
    return render(request, template_name, context)


class MaterialListView(ListView):
    model = Material
    context_object_name = 'items_list'
    # fields = ['material_name','part_number','unit_of_measure']
    # ordering = ['-part_number']


class MaterialDetailView(DetailView):
    model = Material
    fields = ['material_name', 'part_number', 'unit_of_measure']
    context = {"form": 'materials/form.py'}


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    fields = ['material_name', 'part_number', 'unit_of_measure']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     mtl = self.get_object()
    #     if self.request.user == mtl.created_by:
    #         return True
    #     return False


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['material_name', 'part_number', 'unit_of_measure']

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user.username
        return super().form_valid(form)

    # def test_func(self):
    #     mtl = self.get_object()
    #     if self.request.user == mtl.created_by:
    #         return True
    #     return False

class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model=Material
