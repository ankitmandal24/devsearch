from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from . models import Project, Tag
from .forms import ProjectForm
from .utils import SearchProject
# Create your views here.

def projects(request):
    projects, search_query = SearchProject(request)

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects,results)

    projects = paginator.page(page)

    context = {'projects': projects,'search_query': search_query}
    return render(request, "projects.html", context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    print('projectobj:', projectobj)
    return render(request, "single-project.html",{'project':projectobj,'tags': tags})

@login_required(login_url="login")
def createproject(request):
    profile = request.user.profile

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,)
        if form.is_valid():
            profile = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context ={'form': form,}
    return render(request, "project_form.html", context)

@login_required(login_url="login")
def updateproject(request, pk ):
    profile = request.user.profile

    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context ={'form': form,}
    return render(request, "project_form.html", context)

@login_required(login_url="login")
def deleteproject(request, pk):
    profile = request.user.profile

    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, "delete_object.html", context)
