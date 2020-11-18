from django.shortcuts import render

# Create your views here.
def resume_index(request):
    return render(request, "resume/index.html")

def actual_resume(request):
    return render(request, "resume/AnnieWileyResume.html")

def about(request):
    return render(request, "resume/about_me.html")