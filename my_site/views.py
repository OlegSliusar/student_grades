from django.shortcuts import render
# from django.http import HttpResponse

from allactions.models import *

def base(request, id_stg):
    sections = Section.objects.all()
    stages = Stage.objects.filter(fSection=sections[0].id)
    stage = Stage.objects.get(pk=id_stg)
    questions = Question.objects.filter(fStage_id=stage.id)
    all_questions = Question.objects.all()
    next_stage = Stage.objects.get(pk=id_stg+1)
    context = {'stages': stages, 'questions': questions, 'sections': sections, 'stage': stage, 'all_questions': all_questions, 'next_stage':next_stage }
    return render(request, 'base.html', context=context)

# def stage(request):
#     stages = Stage.objects.all()
#     return render(request)
#
