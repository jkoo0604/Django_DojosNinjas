from django.shortcuts import render, redirect
from .models import Dojo, Ninja
from django.db.models import Count

# Create your views here.
def index(request):

    context = {
        'all_dojo': Dojo.objects.all(),
        # 'ninja_count': Dojo.objects.annotate(num_ninjas=Count('ninjas'))
    }
    # print(Dojo.objects.annotate(num_ninjas=Count('ninjas')))
    return render (request, 'index.html',context)


def addDojo(request):
    Dojo.objects.create(name=request.POST['dojoname'],city=request.POST['dojocity'],state=request.POST['dojostate'])

    return redirect('/')


def addNinja(request):
    Ninja.objects.create(first_name=request.POST['ninjafirst'],last_name=request.POST['ninjalast'],dojo_id=int(request.POST['dojolist']))
    # Ninja.objects.create(first_name=request.POST['ninjafirst'],last_name=request.POST['ninjalast'],dojo=Dojo.objects.get(id=int(request.POST['dojolist'])))
    return redirect('/')

def removeDojo(request, removeid):
    deleterecord = Dojo.objects.get(id=removeid)
    deleterecord.delete()
    return redirect('/')