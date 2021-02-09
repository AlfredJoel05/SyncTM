from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

def landingPage_view(request):
    return render(request, "landingpage.html")
    
def detailsPage_view(request):
    link = request.POST.get("link")
    return render(request, 'details.html')
