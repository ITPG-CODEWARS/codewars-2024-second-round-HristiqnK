from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.method == "POST":
        longurl = request.POST.get('longurl')
        code = request.POST.get('code')
        if longurl and code:
            url = URL(longurl=longurl, code=code, username=request.user.username)
            url.save()
    return render(request, "home/index.html")
@login_required
def ShortUrl(request, code):
    url = get_object_or_404(URL, code=code, username=request.user.username)
    return redirect(url.longurl)