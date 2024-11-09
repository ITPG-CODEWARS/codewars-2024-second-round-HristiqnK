from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    if request.method == "POST":
        longurl = request.POST.get('longurl')
        code = request.POST.get('code')
        if longurl and code:
            url = URL(longurl=longurl, code=code)
            url.save()
    return render(request, "home/index.html")

def ShortUrl(reqest, code):
    url = get_object_or_404(URL, code=code)
    return redirect(url.longurl)