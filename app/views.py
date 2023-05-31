from django.shortcuts import render

# Create your views here.

def niru(request):
    
    d={'a':230,'b':45,'c':65}
    return render(request,'niru.html',context=d)

def paru(request):
    d={'a':234,'b':343,'c':76}
    return render(request,'paru.html',context=d)