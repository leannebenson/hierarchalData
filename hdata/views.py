from django.shortcuts import render, reverse, HttpResponseRedirect
from hdata.models import File
from hdata.forms import CreateFileForm, LoginForm
from django.contrib.auth import login, logout, authenticate

def index_view(request):
    files = File.objects.all()
    return render(request,"index.html",{"files":files})

def new_file(request):
    if request.method == 'POST':
        form = CreateFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            file = File.objects.create(
                name=data.get("name"),
                parent=data.get("parent")
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = CreateFileForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request,  "generic_form.html", {"form": form} )

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
