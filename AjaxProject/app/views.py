from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showname(request):
    if request.method == 'POST':
        name = request.POST['myname']
        # return render(request, 'index.html', {'name': name})
        return HttpResponse(f'My Name is <b>{name}</b>')

    else:
        name='No Name'
        return render(request, 'app/index.html', {'name': ''})
    
def ajax_response(request):
    html_code = "<h1>Invalid request</h1>"  # Default response
    try:
        if 'zipcode' in request.GET:
            zipcode = request.GET['zipcode']
            print("Zipcode:", zipcode)  # Log the zipcode
            html_code = f"<h1>Zipcode is {zipcode}</h1>"
    except Exception as e:
        print("Error:", e)
    
    return HttpResponse(html_code)