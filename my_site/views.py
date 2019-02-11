from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from allactions.models import *


@login_required(login_url='')
def base(request, id_sec=1, id_stg=1):
        sections = Section.objects.all()
        stage = Stage.objects.get(pk=id_stg)
        section = Section.objects.get(pk=id_sec)
        stages_in_sec = Stage.objects.filter(fSection=section.id)
        questions = Question.objects.filter(fStage_id=stage.id)
        all_questions = Question.objects.all()
        if(id_stg>1 and id_stg<len(stages_in_sec)):
                next_stage = Stage.objects.get(pk=id_stg+1)
                prev_stage = Stage.objects.get(pk=id_stg-1)
        else:
                next_stage = Stage.objects.get(pk=2)
                prev_stage = Stage.objects.get(pk=1)

        context = {'stages_in_sec': stages_in_sec, 'questions': questions, 'sections': sections, 'stage': stage,
                   'all_questions': all_questions, 'next_stage': next_stage, 'prev_stage': prev_stage,
                   'section': section}

        # A HTTP POST?
        if request.method == 'POST':
                print("Hello user")
                # form = AnswerForm(request.POST)

                # Have we been provided with a valid form?
                # if form.is_valid():
                        # Save the new category to the database.
                        # answer = form.save(commit=False)
                        # answer.fUser = request.user.id
                        # answer.answer_like = request.radio.id
                        # answer.fQuestion = question.id
                        # answer.fGrade = request.grade.id
                        # answer.save()

                        # Redirect to home (/)
                        # return redirect('/')
                # else:
                        # The supplied form contained errors - just print them to the terminal.
                        # print
                        # form.errors
        # else:
                # If the request was not a POST, display the form to enter details.
                # form = AnswerForm()


        return render(request, 'base.html', context=context)
