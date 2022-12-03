from django.shortcuts import render, redirect
from .models import blogTable
from . forms import contactUsers


def home(req):
    database = blogTable.objects.all()
    return render(req, "blog.html", {"database":database})

def content(req, pk):
    database = blogTable.objects.get(id = pk)
    return render (req, 'content.html', {"db": database})

def contact(req):
    form = contactUsers()
    if req.method == "POST":
        form = contactUsers(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'contactus.html', {"form":form})
# Create your views here.
