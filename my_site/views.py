from django.shortcuts import render
# from django.http import HttpResponse

from allactions.models import *

def base(request, id_stg):
    sections = Section.objects.all()
    stages = Stage.objects.all()
    stage = Stage.objects.get(pk=id_stg)
    questions = Question.objects.filter(fStage_id=stage.id)
    return render(request, 'base.html', context={'stages': stages, 'questions': questions, 'sections': sections, 'stage': stage })
#
# def stage(request):
#     stages = Stage.objects.all()
#     return render(request)
#
