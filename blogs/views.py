from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

class CreateBlog(CreateView):
    model = Blog
    template_name = "blogs/create.html"
    fields = ["title", "body", "author"]




class ListBlog(ListView):
    model = Blog
    template_name = "blogs/list.html"

# class ListBlog(ListView):
#     template_name = "blogs/list.html"
#     context_object_name = "object_list"
#     queryset = get_list_or_404(Blog)




class DetailBlog(DetailView):
    model = Blog
    template_name = "blogs/detail.html"
    context_object_name = "example"
            
# def detail_blog(request, pk):
#     example = get_object_or_404(Blog, pk=pk)
#     return render(request, "blogs/detail.html", {"example": example})




class UpdateBlog(UpdateView):
    model = Blog
    template_name = "blogs/edit.html"
    fields = ["title", "body"]




class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blogs/delete.html"
    success_url = reverse_lazy("list")   
