from django.shortcuts import render, redirect
from . models import Todo
from . forms import TodoForm, MailForm
from django.views.decorators.http import require_POST
import datetime, pytz
from django.db import IntegrityError
from django.core.mail import send_mail

prompt= ''
label = 'home'
def home(request):
    global prompt, label
    if(label == 'home'):
        prompt = ''
    label = 'home'
    todo_list = list(Todo.objects.all().order_by('priority')) #pylint: disable=E1101
    print(todo_list)
    listlen = len(todo_list)
    form = TodoForm()
    mform = MailForm()
    date = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  
    context = {'todo_list': todo_list, 
               'form': form,
               'mydate': date,
               'mailform': mform,
               'message': prompt,
               'long': listlen}

    return render(request, 'todo/home.html', context=context)

@require_POST
def addTodo(request):
    global prompt, label
    label = 'addtodo'
    form = TodoForm(request.POST)

    if form.is_valid:
        new_todo = Todo(text=request.POST['text'], priority=request.POST['priority'])
        print(new_todo)
        try:
            new_todo.save()
            prompt = 'Todo Added!'
        except IntegrityError:
            print('duplicate')
            prompt = 'Todo already exists!' 
    else:
        prompt = 'Oops! Please try again!'

    return redirect('home')

def completeTodoToggle(request, todo_id):
    global prompt, label
    label = 'complete'
    prompt = ''
    todo = Todo.objects.get(pk=todo_id)  #pylint: disable=E1101
    if(todo.complete):
        todo.complete = False
        todo.priority = 0
    else:
        todo.complete = True
        todo.priority = 3
    todo.save()

    return redirect('home')

def deleteCompleted(request):
    global prompt, label
    label = 'deletecompleted'
    todo_list = Todo.objects.filter(complete__exact=True)  #pylint: disable=E1101
    if(len(todo_list) > 0):
        todo_list.delete()
        prompt = 'Completed todos deleted!'
    else:
        prompt = 'No todos completed!'
    return redirect('home')

def deleteAll(request):
    global prompt, label
    label = 'deleteall'
    todo_list = Todo.objects.all()  #pylint: disable=E1101
    if(len(todo_list) > 0):
        todo_list.delete()
        prompt = 'All todos deleted!'
    else:
        prompt = 'No todos!'
    return redirect('home')

@require_POST
#set prompt value
def mailAll(request):
    global prompt, label
    label = 'mail'
    todo = Todo.objects.values()  #pylint: disable=E1101
    items = []
    for i in todo:
        flag = ': completed' if i['complete'] else ': incomplete'
        items.append(i['text'] + flag)
    print(items)
    
    form = MailForm(request.POST)

    if form.is_valid:
        notes = request.POST.get('notes','')
        mailto = request.POST.get('mailto','')
        if mailto == '':
            mailto = 'chintan.maniyar.iitb@gmail.com'
        salutation = '\n' + '\nBest Regards,' + '\nChintan Maniyar\nProject Intern\nDept of Computer Science\nIIT Bombay'

        body = notes + '\n'
        for line in items:
            body += '\n' + '-' + line

        body += salutation       
        try:
            send_mail(
                'Your Todo List',
                body,
                'seminarhallbs@gmail.com',
                [mailto],
                fail_silently=True,
            )
            prompt = 'Mail sent!'
        except:
            prompt = 'Oops! Please try again!'
        
    else:
        prompt = 'Oops! Please try again!'

    return redirect('home')
