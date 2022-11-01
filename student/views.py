from django.shortcuts import render
from .forms import StudForm,sform
from .models import stud_form

# Create your views here.
def show(requests):
    return render(requests,"home.html")



def register(request):
    title="New Student Registration"
    form = StudForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        clas=form.cleaned_data['s_class']
        address=form.cleaned_data['s_address']
        school=form.cleaned_data['s_school']
        mail=form.cleaned_data['s_email']
        email=stud_form.objects.filter(s_email=mail)
        if len(email)>0:
            return render(request, 'ack.html', {"title": "Student Already exists..Try with other E-mail"})
        else:
            p=stud_form(s_name=name,s_class=clas,s_address=address,s_school=school,s_email=email)
            p.save()
            return render(request, 'ack.html',{"title":"Register successfully"})

    context={
        "title":title,
        "form":form,
    }
    return render(request,'register.html',context)

def existing(request):
    title="All Registered Student"
    queryset=stud_form.objects.all()
    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context)
def search(request):
    title="Search Student"
    form=sform(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud_form.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request, 'ack.html',{'title':'Student Details Not Found Please Correct Enter Correct Data'})

        context={
            'title':title,
            'queryset':queryset,

        }
        return  render(request,'existing.html',context)


    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)

def dropout(request):
    title="Drop Out"
    form=sform(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud_form.objects.filter(s_name=name).delete()
        return render(request,'ack.html',{'title':"student remove from your database"})

    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)




