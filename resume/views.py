from django.shortcuts import render, redirect

def resume_index(request):
    return render(request, "resume/index.html")

def actual_resume(request):
    return render(request, "resume/resume_pane.html")

def about(request):
    return render(request, "resume/about_me.html")