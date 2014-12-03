# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from studentapp.models.groups import Group
from studentapp.forms import GroupForm

# Create your views here.

def groups(request, page_number = 1):
    table_group = Group.objects.all()
    paginator = Paginator(table_group, 3)
    page = request.GET.get('page')
    try:
        table_group = paginator.page(page)
    except PageNotAnInteger:
        table_group = paginator.page(1)
    except EmptyPage:
        table_group = paginator.page(paginator.num_pages)
    return render_to_response('groups.html',
        {'table_group': table_group},
        context_instance=RequestContext(request))

def addgroup(request):
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(u'/groups/?status_message=Група успішно додана!')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})



def edit_group(request, group_id):
    table_group = Group.objects.get(id=group_id)
    table_student = Student.objects.all()
    errors = {}
    error = {}
    if request.POST.get('name_group', '').strip() == '':
        errors['name_group'] = 'Введіть будь ласка назву групи'
        error['name_group'] = 'поле Назва групи обов’язкове'
    if request.POST.get('submit'):
        if errors:
            return render_to_response('edit_group.html',
                {'errors': errors,
                'error': error},
                context_instance=RequestContext(request))
        else:
            if request.POST.get('king_group', '').strip() == '':
                group_object = Group(id = group_id,
                                    name_group = request.POST['name_group'],
                                    king_group = None)
            else:
                group_object = Group(id = group_id,
                                    name_group = request.POST['name_group'],
                                    king_group = Student(pk=request.POST['king_group']))
            group_object.save()
            return redirect(u'/groups/?status_message=Група успішно відредагована!')
    return render_to_response('edit_group.html', {
                                                'table_student': table_student,
                                                'table_group': table_group},
                                                context_instance=RequestContext(request))

def group_delete(request, group_id):
    g = Group.objects.get(id=group_id)
    g.delete()
    return redirect('/groups/?status_message=Група успішно видалена!')