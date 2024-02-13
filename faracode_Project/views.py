from django.shortcuts import render
from projects_app.models import Project
from contactus_app.models import Footer, Message

def home(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')
        Message.objects.create(fullname=fullname, email=email, sub=sub, body=body)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects':projects, 'footer':footer})

