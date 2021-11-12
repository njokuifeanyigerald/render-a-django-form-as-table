from django.shortcuts import redirect, render
from .models import DataModel
from .forms import DataForm

def home(request):
    form = DataForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            department = form.cleaned_data['department']
            age = form.cleaned_data['age']
            queryset = DataModel(name=name,department=department, age=age)
            queryset.save()
            return redirect('home')
        else:
            pass
            
    context = {
        'form':form
    }
    return render(request, 'app/home.html', context)
