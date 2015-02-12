# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from studentapp.models.groups import Group
from studentapp.models.students import Student
from studentapp.forms import GroupFormAdd, GroupFormEdit
# Create your views here.

def groups_list(request, page_number=1):
    table_group = Group.objects.all()
    paginator = Paginator(table_group, 3)
    page = request.GET.get('page')
    try:
        table_group = paginator.page(page)
    except PageNotAnInteger:
        table_group = paginator.page(1)
    except EmptyPage:
        table_group = paginator.page(paginator.num_pages)
    return render_to_response('groups/groups_list.html',
        {'table_group': table_group},
        context_instance=RequestContext(request))

def add_group(request):
    if request.POST:
        form = GroupFormAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(u'%s?status_message=Група успішно додана!' %
                            reverse('group_list'))
    else:
        form = GroupFormAdd()
    return render(request, 'groups/add_group.html',
        {'form': form})

def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = GroupFormEdit(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect(u'%s?status_message=Група успішно відредагована!' %
                            reverse('group_list'))
    else:
        form = GroupFormEdit(instance=group)
    return render_to_response('groups/edit_group.html',
        {'form': form,
        'group': group},
        context_instance=RequestContext(request))

def group_delete(request, group_id):
    g = Group.objects.get(id=group_id)
    try:
        g.delete()
    except:
        return redirect(u'%s?status_message=Неможливо видалити, можливо в цій групі є студенти, спочатку видаліть їх!' %
                    reverse('group_list'))
    return redirect(u'%s?status_message=Група успішно видалена!' %
                    reverse('group_list'))