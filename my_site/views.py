from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from allactions.models import *


@login_required(login_url='')
def base(request, id_stg=1):
        sections = Section.objects.all()
        stages = Stage.objects.all()
        stage_sk = Stage.objects.filter(fSection=1).first()
        stage_act = Stage.objects.filter(fSection=2).first()
        stage = Stage.objects.get(pk=id_stg)
        questions = Question.objects.filter(fStage_id=stage.id)
        all_questions = Question.objects.all()

        if(id_stg>1 and id_stg<len(stages)):
                next_stage = Stage.objects.get(pk=id_stg+1)
                prev_stage = Stage.objects.get(pk=id_stg-1)
        else:
                next_stage = Stage.objects.get(pk=2)
                prev_stage = Stage.objects.get(pk=1)

        context = {'stages': stages, 'questions': questions, 'sections': sections, 'stage': stage,
                   'all_questions': all_questions, 'next_stage': next_stage, 'prev_stage': prev_stage,
                   'stage_sk': stage_sk, 'stage_act': stage_act}
        return render(request, 'base.html', context=context)

