from django.shortcuts import render,redirect
from django.views import View

from cbvapp.forms import ReviewForm

# Create your views here.

class HomeView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,'cbvapp/index.html',{'form':form})
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
           
