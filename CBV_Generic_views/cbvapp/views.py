from django.shortcuts import render,redirect
from django.views import View

from cbvapp.forms import ReviewForm

# Create your views here.

# class HomeView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,'cbvapp/index.html',{'form':form})
    
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
        
#         return redirect('/')
from .models import Review
from django.views.generic.edit import FormView
class HomeView(FormView):
    form_class = ReviewForm
    template_name = 'cbvapp/index.html'
    # model = Review
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

from .models import Review
from django.views.generic import ListView

class FirstpageView(ListView):
    template_name = "cbvapp/home.html"
    model = Review

    def get_queryset(self):
        allobj = super().get_queryset()
        review = allobj.filter(rating__lt=3)
        return review