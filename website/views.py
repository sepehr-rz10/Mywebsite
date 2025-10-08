from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def index_view(request):
    return render(request , 'website/index.html')
def about_view(request):
    return render(request , 'website/about.html')
def contact_view(request):
    return render(request , 'website/contact.html')



# def about_view(request):
    # return HttpResponse('<h1>About Page</h1>')
# def contact_view(request):
    # return JsonResponse({'name' : 'sepehr rezaei'})
# Create your views here.
