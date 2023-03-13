from django.shortcuts import render

# Create your views here.
def kohli(request):
    d={'score':55}
    return render(request,'match.html',context=d)