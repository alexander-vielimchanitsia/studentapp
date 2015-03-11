# -*- coding: utf-8 -*-

from django.core.management.base import LabelCommand

from studentapp.models import Group, Student


class Command(LabelCommand):
    args = '"<name_group>"'
    help = 'Takes the name of the group and gives a list of students'

    requires_model_validation = False
    can_import_settings = True

    def handle_label(self, name_group, **options):
        # argument is decoding in unicode
        name_group = name_group.decode('utf8')

        try:
            group = Group.objects.get(name_group=name_group)
            # order by the group
            students = Student.objects.filter(stud_group=group.id)

            # check whether the students in this group
            if len(students) > 0:
                self.stdout.write('All students in the group "%s":' % name_group)
                for student in students:
                    self.stdout.write(u'%s' % student)

            # if no students in this group
            else:
                self.stdout.write('No students in group "%s"' % name_group)

        except Group.DoesNotExist:
            self.stdout.write('Group "%s" does not exist' % name_group)