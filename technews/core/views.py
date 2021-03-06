from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# def index(request):
#     return render(request, 'core/index.html')

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # console.log("will register user!")
            user = form.save()
            login(request, user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form':form})
