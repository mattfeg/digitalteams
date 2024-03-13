from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'dtapp/index.html')

def notFoundPage(request, exception):
    return render(request, 'dtapp/notFoundPage.html')