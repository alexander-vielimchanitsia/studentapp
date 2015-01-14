from django.core.management.base import BaseCommand, CommandError, LabelCommand

from studentapp.models import Group, Student


class Command(LabelCommand):
    help = 'takes the name of the group and gives a list of students'

    requires_model_validation = False
    can_import_settings = True

    def handle_label(self, name_group, **options):
        try:
            group = Group.objects.get(name_group=name_group)
        except:
            raise CommandError('This is group DoesNotExist')
        students = Student.objects.filter(stud_group=group.id)

        self.stdout.write('All students in group "%s"' % students)
