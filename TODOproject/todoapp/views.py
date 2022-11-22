from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

class Taskdeleteview(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class Taskupdateview(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'edit.html'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk:self.object.id'})
class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

# def details(request):
#
#     return render(request,'detail.html',)

def delete(request,taskid):
    if request.method=='POST':
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})