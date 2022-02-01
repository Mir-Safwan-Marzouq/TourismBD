from django.shortcuts import render
from django.http import HttpResponse
from TourismBD.models import Division,District_info,District_travel,Feedback


# Create your views here.
def index(request):
    dictionary={}
    return render(request,'TourismBD/index.html',dictionary)

def division(request,b):
    div=Division.objects.get(pk=b)
    distrct=District_info.objects.filter(divisionName=b)
    dictionary ={'div':div,'distrct':distrct}
    return render(request,'TourismBD/division.html',dictionary)

def district(request,z):
    district=District_info.objects.get(pk=z)
    dst=District_travel.objects.filter(districtName=z).order_by('name')
    dictionary={'dst':dst, 'district':district}
    return render(request,'TourismBD/district.html',dictionary)

def search_district(request):
    if request.method == "POST":
        searched=request.POST['searched']
        place=District_info.objects.filter(name__icontains=searched)
        area=District_travel.objects.filter().order_by('name')
        dictionary={'searched':searched,'place':place,'area':area}
        return render(request,'TourismBD/districtSearch.html',dictionary)
    else:
        dictionary={}
        return render(request,'TourismBD/districtSearch.html',dictionary)

def feedback(request):
    # print('Hello The form has been submitted')
    fullName=request.POST.get('fullName', False)
    emailAddress=request.POST.get('emailAddress', False)
    feedbackText=request.POST.get('feedbackText', False)

    feedback=Feedback(fullName=fullName,emailAddress=emailAddress,feedbackText=feedbackText)
    feedback.save()
    dictionary ={}
    return render(request,'TourismBD/feedback.html',dictionary)

def about(request):
    dictionary ={}
    return render(request,'TourismBD/about.html',dictionary)

def destination(request,dest):
    destin=District_travel.objects.get(pk=dest)
    dictionary={'destin':destin}
    return render(request,'TourismBD/place.html',dictionary)
