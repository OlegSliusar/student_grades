from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from allactions.models import *
from answers.models import Answer
from users.models import User


@login_required(login_url='')
def base(request, id_sec=1, id_stg=1):
        sections = Section.objects.all()
        stage = Stage.objects.get(pk=id_stg)
        section = Section.objects.get(pk=id_sec)
        stages_in_sec = Stage.objects.filter(fSection=section.id)
        questions = Question.objects.filter(fStage_id=stage.id)
        all_questions = Question.objects.all()
        grades = Grade.objects.all()
        if(id_stg>1 and id_stg<len(stages_in_sec)):
                next_stage = Stage.objects.get(pk=id_stg+1)
                prev_stage = Stage.objects.get(pk=id_stg-1)
        else:
                next_stage = Stage.objects.get(pk=2)
                prev_stage = Stage.objects.get(pk=1)

        context = {'stages_in_sec': stages_in_sec, 'questions': questions, 'sections': sections, 'stage': stage,
                   'all_questions': all_questions, 'next_stage': next_stage, 'prev_stage': prev_stage,
                   'section': section, 'grades': grades}

        # A HTTP POST?
        if request.method == 'POST':
                print("Hello user")
                answer = Answer()
                answer.fUser = User.objects.get(pk=1)
                answer.answer_like = request.POST.get('choice')
                answer.fQuestion_id = request.POST.get('question')
                grade = request.POST.getlist('grade')
                print(str(grade[0]))
                grade_list = []
                # for grade in grades:
                #         grade_list.append(Grade.objects.get(name=grade))
                print(grade)
                grade = Grade.objects.get(name=grade[0])
                print(grade)
                answer.fGrade = grade
                answer.save()

                # Redirect to home (/)
                return redirect('/')


        return render(request, 'base.html', context=context)
