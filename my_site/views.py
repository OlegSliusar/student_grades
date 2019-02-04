from django.shortcuts import render
# from django.http import HttpResponse

from allactions.models import Stage
from allactions.models import Section

def base(request):
    # sections = Section.objects.all()
    stages = Stage.objects.all()

    return render(request, 'stages.html', context={'stages': stages})

# def stage(request):
#     stages = Stage.objects.all()
#     return render(request)
#
