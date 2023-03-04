from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, Http404

from .models import Note
from .forms import NoteForm, SearchForm

# Create your views here.

@login_required
def publish(request, _id):
    note = Note.objects.get(id=_id)
    note.status=1
    note.save()
    return redirect('note:note')

@login_required
def editnote(request, _id):
    post = Note.objects.get(id=_id)
    if request.method != 'POST':
        form = NoteForm(instance=post)
    else:
        form = NoteForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('note:detailnote', args=[post.id]))
    context = {'post': post, 'form': form}
    return render(request, 'editnote.html', context)

@login_required
def deletenote(request, _id):
    deletepost=Note.objects.get(id=_id)
    deletepost.delete()
    return HttpResponseRedirect(reverse('note:note'))

@login_required
def draftdetail(request,_id):
    try:
        data =Note.objects.get(id =_id)
    except Note.DoesNotExist:
        raise Http404('Data does not exist')
     
    context = {
            'data':data
        }
    return render(request,'detaildraft.html', context)

@login_required
def notedetail(request,_id):
    try:
        data =Note.objects.get(id =_id)
    except Note.DoesNotExist:
        raise Http404('Data does not exist')
     
    context = {
            'data':data
        }
    return render(request,'detailnote.html', context)

def index(request):
    return render(request, 'index.html')

@login_required
def draft(request):
    dataset=Note.objects.all().filter(status=0, owner=request.user).order_by('-date_updated')
    paginator = Paginator(dataset, 5)
    page = request.GET.get('page')
    try:
        dataset = paginator.page(page)
    except PageNotAnInteger:
        dataset = paginator.page(1)
    except EmptyPage:
        dataset = paginator.page(paginator.num_pages)
    try:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['topic']
                entry = Note.objects.filter(owner=request.user, status=0).get(topic=topic)
                return redirect(reverse('note:detailnote', args=[entry.id]))
    except Note.DoesNotExist:
        raise Http404
    else:
        form = SearchForm()
        context = {
            'dataset':dataset,
            'form':form,
            'page': page,
        }
        return render(request,'draft.html',context)

@login_required
def note(request):
    dataset = Note.objects.all().filter(status=1, owner=request.user).order_by('-date_updated')
    paginator = Paginator(dataset, 3)
    page = request.GET.get('page')
    try:
        dataset = paginator.page(page)
    except PageNotAnInteger:
        dataset = paginator.page(1)
    except EmptyPage:
        dataset = paginator.page(paginator.num_pages)
    try:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                topic = form.cleaned_data['topic']
                entry = Note.objects.filter(owner=request.user, status=1).get(topic=topic)
                return redirect(reverse('note:detailnote', args=[entry.id]))
    except Note.DoesNotExist:
        raise Http404
    else:
        form = SearchForm()
        context = {
            'dataset':dataset,
            'form':form,
            'page': page,
        }
        return render(request,'note.html',context)

@login_required
def addnote(request):
    if request.method != 'POST':
        form = NoteForm() 
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('note:note'))
    context = {'form': form}
    return render(request, 'addnote.html', context)
