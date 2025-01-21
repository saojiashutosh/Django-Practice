from django.shortcuts import render

# Create your views here.
def home(request):
    if request.session :
        count = int(request.session.get('counter',0))
        count += 1
        request.session['counter'] = count
        respose = render(request,'sessionapp/index.html')
        return respose

    else :
        respose = render(request,'sessionapp/index.html')
        request.session['counter'] = 0
        return respose