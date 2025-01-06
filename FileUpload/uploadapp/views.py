import os ,random ,string
from django.shortcuts import render

# Create your views here.
def randomfilename(file_extension):
    while True:
        filename = ''.join(random.choices(string.ascii_letters, k=6))
        filename = filename +'.'+file_extension
        if os.path.exists(f'media/uploadapp/{filename}'):
            continue
        break
    return filename


def savefile(filedatachunks):
    file_extension = filedatachunks.name.split('.')[-1]
    filename = randomfilename(file_extension)
    with open(f"media/uploadapp/{filename}", "wb+") as fobj:
        for chunk in filedatachunks.chunks():
            fobj.write(chunk)

    return filedatachunks.name

def home(request):
    msg=""
    if request.method == "POST":
        savefile(request.FILES['filedata'])
        msg = f"Hi {request.POST['name']}  your file is uploaded"
    return render(request,"uploadapp/index.html",{'msg':msg})