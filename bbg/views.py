import json
from .forms import BbgprojectForm
from accounts.utils import detectUser, send_verification_email,send_confirm_email
from accounts.forms import UserForm
from accounts.utils import send_mail,send_notification
from django.shortcuts import render, redirect,get_object_or_404,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from main.filters import Bbgprojectfilter
from .models import Bbgproject,BbgImage
from expads.models import Category,Countrycode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied

# Restrict the customer from accessing the vendor page


def bbglist(request):
    #print('BBG Home page')
    bbgproject_filter = Bbgprojectfilter(request.GET, queryset=Bbgproject.objects.all().filter(is_active=True))
    bbgprojects = bbgproject_filter.qs
    bbgproject_count = bbgprojects.count()
    paginator = Paginator(bbgprojects, 10)
    page = request.GET.get('page')
    paged_bbgprojects = paginator.get_page(page)
    bbgproject_count = bbgprojects.count()
    #print(bbgproject_count)
    context = {
        'form':bbgproject_filter.form,
        'bbgprojects_list':bbgproject_filter.qs,
        'bbgprojects':paged_bbgprojects,
        'bbgproject_count':bbgproject_count}    
    return render(request, 'bbg/bbglist.html', context)    



@login_required(login_url='login')
def bbgads(request):
    print("Here came BBGADS Starting")
    form=BbgprojectForm()
    if request.method == "POST":
        form=BbgprojectForm(request.POST,request.FILES)
        images_list = request.FILES.getlist('images')
        request.POST._mutable = True
        form.data['user']=request.user
        form.data['is_active']=True
        if form.is_valid():
            newform=form.save()
            print("Success")
            bbgproject = Bbgproject.objects.get(id=newform.id)
            print(bbgproject)
            print(images_list)
            for image in images_list:
                BbgImage_images = BbgImage.objects.create(
                    bbgprojects= bbgproject,
                    images = image
                )
                print("Saved images")
            messages.success(request, 'BBG Ad added successfully.')
            return redirect('home')
        #else:
            #messages.error(request,'Enter Valid Data')
            #return redirect(request.META['HTTP_REFERER'])
            #return HttpResponse('Form Not Valid')
    else:
        print("Here came BBGADS Ending")
        form = BbgprojectForm()
    countrycodes=Countrycode.objects.all()
    context = {'form':form,'countrycodes':countrycodes}
    return render(request, 'bbg/bbgads.html',context)



def bbgdetail(request,id):
    print("starting Dtail")
    bbgproject =  get_object_or_404(Bbgproject,id=id)
    bbgImageImage_list =BbgImage.objects.filter(bbgprojects=bbgproject).prefetch_related('bbgprojects')
    print(bbgproject)
    if request.user==bbgproject.user:
        uservalue=True
    else:
        uservalue=False
    print("Dtail")
    context = {'bbgprojects':bbgproject,'bbgImageImage_list': bbgImageImage_list,'uservalue':uservalue}
    return render(request,'bbg/bbgdetails.html',context)



 
"""
def bbglist(request, slug=None):
    categories = None
    expatads = None
    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        bbgproject_filter = Bbgprojectfilter(request.GET, queryset=Bbgproject.objects.all().filter(category=categories,is_active=True))
        bbgprojects = bbgproject_filter.qs
        paginator = Paginator(bbgprojects, 4)
        page = request.GET.get('page')
        paged_bbgprojects = paginator.get_page(page)
        bbgproject_count = bbgprojects.count()
    else:
        bbgproject_filter = Bbgprojectfilter(request.GET, queryset=Bbgproject.objects.all().filter(is_active=True))
        print(bbgproject_filter.qs)
        bbgprojects = bbgproject_filter.qs
        paginator = Paginator(bbgprojects, 4)
        page = request.GET.get('page')
        paged_bbgprojects = paginator.get_page(page)
        bbgproject_count = bbgprojects.count()

        context = {
            'bbgprojects': paged_bbgprojects,
            'bbgproject_count': bbgproject_count,
            'form': bbgproject_filter.form,
            'bbgprojects_list': bbgproject_filter.qs,
            }
    return render(request, 'bbg/bbglist.html', context) """