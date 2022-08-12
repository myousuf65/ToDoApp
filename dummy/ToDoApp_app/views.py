from django.shortcuts import render , HttpResponse, redirect
from .forms import ToDoApp_form
from .UpdateForm import UpdateForm
from .models import ToDoApp_model
# Create your views here.

def FormView(request):
    form = ToDoApp_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = ToDoApp_form()
    objects = ToDoApp_model.objects.all()
    context = {
        'form': form,
        'objects': objects
    }
    return render(request, 'index.html' , context)

def deleteView(request , item_id):
    item = ToDoApp_model.objects.get(pk=item_id)
    item.delete()
    return redirect('/')

def updateView(request, item_id):
    item = ToDoApp_model.objects.get(pk=item_id)
    form = UpdateForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'item' : item,
        'form' : form,
    }
    return render(request, 'update.html' , context)