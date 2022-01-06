from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'wall_message': Wall_Messages.objects.all()
    }
    return render(request, 'success.html', context)


def register(request):
    # if request.method == 'POST':
        print(request.POST)
        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/success')
        
        
def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email = request.POST['email'])
        # print(logged_user)
        # print(User.objects.all())
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            # print(logged_user)
            # print(logged_user.password, request.POST['password'])
            if logged_user.password == request.POST['password']:
                request.session['user'] = logged_user.first_name
                request.session['id'] = logged_user.id
                return redirect('/success')
    return redirect('/')

def post_msg(request):
    Wall_Messages.objects.create(message = request.POST['message'], poster = User.objects.get(id=request.session['id']))
    return redirect('/success')

def delete_post(request, id):
    delete_a_post = Wall_Messages.objects.get(id=id)
    delete_a_post.delete()
    return redirect('/success')

def post_comment(request, id):
    poster = User.objects.get(id=request.session['id'])
    message = Wall_Messages.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/success')

def user_profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Messages.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def delete_comment(request, id):
    deleted = Comment.objects.get(id=id)
    deleted.delete()
    return redirect('/success')

def edit(request, id):
    edit_user = User.objects.get(id=id)
    if request.method == 'POST':
        edit_user.first_name = request.POST['first_name']
        edit_user.last_name = request.POST['last_name']
        edit_user.email = request.POST['email']
        edit_user.save()
        return redirect('/success') 
    return redirect('/edit_profile/<int:id>')
    
def edit_profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def myprofile(request,id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'myprofile.html', context)

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')


