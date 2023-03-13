from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'score':70}
    return render(request,'match.html',context=d)