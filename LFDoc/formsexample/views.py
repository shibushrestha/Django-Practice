from django.shortcuts import render
from formsexample.forms import PersonForm, CreatePersonForm
from .models import Person

# THIS VIEW IS FOR THE NORMAL FORM
def create_person(request):
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            email = form.cleaned_data.get('email')
            comments = form.cleaned_data.get('comments')

            person = Person.objects.create_person(username=username, 
                first_name=first_name, last_name=last_name, 
                date_of_birth=date_of_birth, 
                email=email, comments=comments)
    else:
        form = CreatePersonForm()
    return render(request, 'formsexample/register.html', {'form':form})


# THIS VIEW IS FOR THE MODELFORM    
def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            email = form.cleaned_data.get('email')
            comments = form.cleaned_data.get('comments')
            form.save()        
    else:
        form = PersonForm(label_suffix='')
    return render(request, 'formsexample/index.html', {'form':form})

