from django.shortcuts import render , HttpResponse
from datetime import datetime
from myapp.models import Contact

# Create your views here.




def index(request):
   context ={
       'varible1': 'heyyy hello i am prathamesh...',
       'varible2': 'and this is myt second varible'
   }
   
   return  render(request,'index.html', context)
    # return HttpResponse("hello world")



def about(request):
   return  render(request,'about.html')

def contact(request):
   if request.method =='POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      contact = Contact(name = name, email= email, phone = phone, subject=subject,message=message, date = datetime.today())
      contact.save()
   return  render(request,'contact.html')

def services(request):
    return  render(request,'services.html' )