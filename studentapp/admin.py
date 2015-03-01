# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from models import Student, Group


class StudentFormAdmin(ModelForm):

    def clean_stud_group(self):
        """Check if student is king_group in any group.

        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        groups = Group.objects.filter(king_group=self.instance)
        if len(groups) > 0 and \
            self.cleaned_data['stud_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.',
                code='invalid')

        return self.cleaned_data['stud_group']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'stud_group']
    list_display_links = ['last_name', 'first_name']
    ordering = ['last_name']
    list_filter = ['stud_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('edit_student', kwargs={'pk': obj.id})


class GroupFormAdmin(ModelForm):

    def clean_king_group(self):
        #Check if student in the group.
        student = Student.objects.filter(stud_group=self.instance)
        if not self.cleaned_data['king_group'] == None and \
            self.cleaned_data['king_group'] != student:
            raise ValidationError(u'Студент не є учасником цієї групи.',
                code='invalid')

        return self.cleaned_data['king_group']

class GroupAdmin(admin.ModelAdmin):
    form = GroupFormAdmin


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)