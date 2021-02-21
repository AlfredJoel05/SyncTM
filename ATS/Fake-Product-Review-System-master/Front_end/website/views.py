from django.shortcuts import render

def landingPage_view(request):
    return render(request, "landingpage.html")
    
def detailsPage_view(request):
    link = request.POST.get("link")
    return render(request, 'details.html')
