from django.shortcuts import render,redirect
from game.models import Topic,Game_log
from django.contrib import messages
from datetime import datetime

# Create your views here.
def main(request):
    return redirect('/home')


def home_page(request):
    return render(request, 'home.html', {'title': 'Home Page'})


def topics_page(request):
    if not request.user.id:
        messages.info(request,'Please login to start quizzing')
        return redirect('user:login')

    if request.method == 'POST':
        choice= request.POST['radioDiff']
        choice_list= choice.split(':')
        id,difficulty= choice_list[0],choice_list[1]
        return redirect('game:play',id=id, difficulty=difficulty)
    else:
        topics= Topic.objects.all()
        return render(request,'topics.html',{'title': 'Choose Topics', 'topics':topics})


def create_url(cat,diff):
    return "https://opentdb.com/api.php?amount=10&category={}&difficulty={}&type=multiple".format(cat,diff)

def log_game(request,id,difficulty):
    user_id= request.user.id
    topic_id = id
    level= difficulty
    date_time= datetime.strftime(datetime.today(), "%d-%m-%Y %H:%M:%S")
    score= request.POST['score']
    try:
        gl= Game_log(topic=topic_id, level=level, user_id= user_id, datetime=date_time,score=score)
        gl.save()
        return True
    except Exception as e:
        messages.error(request, 'Error: {}'.format(e))
        return False


def play_quiz(request,id,difficulty):
    if not request.user.id:
        messages.info(request,'please login to start quizzing')
        return redirect('user:login')

    if request.method == "POST":
        #score= request.POST['score']
        if not log_game(request,id,difficulty):
            return redirect('game:topics')
        return redirect('game:end')

    if id<=0 or difficulty not in ['easy','medium','hard']:
        messages.error(request,'Some error occurred. Please try again')
        return redirect('game:topics')

    category= Topic.objects.get(id=id).category
    if not category:
        messages.error(request,'Invalid topic! Please try again')
        return redirect('game:topics')

    url= create_url(category,difficulty)

    return render(request,'game.html',{'url':url, 'title':'Play Quiz'})


def end_game(request):
    print('ending')
    game_data= Game_log.objects.filter(user_id=request.user.id).last()
    if not game_data:
        messages.error(request,'Quiz information is not found!')
        return redirect('game:topics')

    topic= Topic.objects.get(id= game_data.topic)
    if not topic:
        messages.error(request,'Topic information was not found')
        return redirect('game:topics')

    return render(request,'end.html',{'title': 'Thank You', 'game_data':game_data, 'topic':topic})