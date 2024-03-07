from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q

def home(request):

   student = Student.objects.all().order_by('first_name')
   count = Student.objects.all().count()
   context = {

      'student':student,
      'count' :count
    }
   return render(request,'home.html',context)


def add(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def delete(request):

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)
        student.delete()
        
    return redirect('home')

def details(request,id):
    student_details = Student.objects.get(id=id)
    context = {
        'details':student_details,
    }
    return render(request,'details.html',context)
    
def search(request):

    if request.POST.get('key') != None:

        search_key = request.POST.get('key')
        
    else:    
        search_key=''

    student = Student.objects.filter( Q(first_name__istartswith = search_key) | Q(last_name__istartswith = search_key))
    context  = {
            'student':student
    }

    return render(request,'home.html',context)

def edit(request,id):

    detaile = Student.objects.get(id=id)
    form = StudentForm(instance=detaile)

    if request.method == 'POST':

        form = StudentForm(request.POST,instance=detaile)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=StudentForm(instance=detaile)

    context = {
        'form':form,
    }

    return render(request,'edit.html',context)
    
