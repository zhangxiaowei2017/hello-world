from django.shortcuts import render
def index(request):
    print("execute index request")
    return render(request,'index.html')
