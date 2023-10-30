from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.utils.crypto import get_random_string

# Create your views here.
def home(request):

    if request.method == "POST":
        form = makeShortURLForm(request.POST)
        if form.is_valid():
            surl = form.save()
            temp_short = get_random_string(length=7)
            check = lsurls.objects.filter(short=temp_short)
            while check.exists():
                temp_short = get_random_string(length=7)
                check = lsurls.objects.filter(short=temp_short)
            surl.short = temp_short
            surl.save()
            return redirect("all")

    form = makeShortURLForm()
    variables = {
        "form":form,
    }
    return render(request,"home.html",variables)

def all(request):
    links = lsurls.objects.all().order_by("-created")
    variables={
        "links":links
    }
    return render(request,"all.html",variables)

def redir(request,key):
    if lsurls.objects.filter(short=key).exists():
        link = lsurls.objects.get(short=key)
        return HttpResponseRedirect(link.long)
    else:
        return redirect("all")
