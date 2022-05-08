from django.shortcuts import render

def welcomehome(request):
    # print(dir(request)) 
    return render(request, 'welcomehome/index.html')