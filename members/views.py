from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q

# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())def 
# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse (template.render(context,request))
def details(request ,slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse (template.render())
def testing(request):
    mymembers = Member.objects.all().order_by('lastname','-id').values()
#     # mydata = Member.objects.filter(firstname__startswith='E').values()
#     # mydata = Member.objects.filter(firstname='Paul').values() | Member.objects.filter(firstname='Brian').values()
#     # mydata= Member.objects.filter(Q (firstname='Teddy') | Q(firstname='Patrick')).values()
    template=loader.get_template('template.html')
    context ={
        'mymembers' : mymembers
    }
#     #     'greeting' : 3
#     # }
#     #   'cars': [
#     #   {
#     #     'brand': 'Ford',
#     #     'model': 'Mustang',
#     #     'year': '1964',
#     #   },
#     #   {
#     #     'brand': 'Ford',
#     #     'model': 'Bronco',
#     #     'year': '1970',
#     #   },
#     #   {
#     #     'brand': 'Volvo',
#     #     'model': 'P1800',
#     #     'year': '1964',
#     #   }]
#     # }
#     # context={
#     #     'fruits' :['Apple','Banana','Cherry','Kiwi'],
#     #     # 'firstname':'Tobias Onyango'
#     # }
    return HttpResponse(template.render(context,request))