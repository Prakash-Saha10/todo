from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO
from django.contrib.auth import authenticate,login,logout
#from todo.models import edit_todo



def signup(request):
    if request.method =='POST':
     fnm=request.POST.get('fnm')
     emailid=request.POST.get('email')
     pwd=request.POST.get('pwd')
     print(fnm,emailid,pwd)
     my_user=User.objects.create_user(fnm,emailid,pwd)
     my_user.save()
     return redirect('/loginn')
    return render(request,'signup.html')

def login_view(request):
    if request.method =='POST':
       fnm=request.POST.get('fnm')
       pwd=request.POST.get('pwd')
       print(fnm,pwd)
       user=authenticate(request,username=fnm,password=pwd)
       if user is not None:
            login(request,user)
            return redirect('/todo')
       else:
          return redirect('/loginn')
    return render(request,'loginn.html')

def todo(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            print(title)
            obj = models.TODO(title=title, user=request.user)  # ✅ FIXED
            obj.save()
            return redirect('/todo')  # ✅ FIXED
    
        # GET request — show todos
        res = models.TODO.objects.filter(user=request.user)
        return render(request, 'todo.html', {'res': res})
   

def signout_view(request):
    logout(request)
    return redirect('/signup') 



def edit_todo(request, srno):
    obj = get_object_or_404(TODO, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        obj.title = title
        obj.save()
        return redirect('/todo')

    res = TODO.objects.filter(user=request.user).order_by('date')
    return render(request, 'edit_todo.html', {'obj': obj, 'res': res})