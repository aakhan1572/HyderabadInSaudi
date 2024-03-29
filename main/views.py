from django.shortcuts import render
#from main.forms import ExpatadFilterform
from expads.models import Expatad
from .filters import Expatadfilter

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def home(request):
    print('Coming Home page')
    expatad_filter = Expatadfilter(request.GET, queryset=Expatad.objects.all().filter(is_active=True))
    #print(expatad_filter)
    expatads = expatad_filter.qs
    expatad_count = expatads.count()
    #expatad_count = expatad_filter.qs.count()
    
    #expatads = expatad_filter.qs
    paginator = Paginator(expatads, 12)
    page = request.GET.get('page')
    paged_expatads = paginator.get_page(page)
    expatad_count = expatads.count()
    context = {
        'form' : expatad_filter.form,
        'expatads_list': expatad_filter.qs,
        'expatads': paged_expatads,
        'expatad_count' : expatad_count,
    }
    print('Filter using')
    return render(request, 'home.html', context)

