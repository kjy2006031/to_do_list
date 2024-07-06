from django.shortcuts import render

def index(request):
    print("작동")
    return render(request, "index.html")