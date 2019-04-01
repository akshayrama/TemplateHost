from django.shortcuts import render

# Create your views here.
def index (request):
    dict = { 'text': "hello world" , 'number': 600 }
    return render(request,'basictempapp/index.html',context = dict)

def other(request):
    return render(request,'basictempapp/other.html')

def relurltemp ( request):
    return render(request,'basictempapp/relurltemp.html')
