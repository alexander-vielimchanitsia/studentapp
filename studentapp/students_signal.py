# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format = u'[%(asctime)s]  %(message)s',
    level = logging.INFO, filename = u'students.log')


def student_save_handler(sender, **kwargs):
    if kwargs['created']:
        details_text = u'Студент був створений'
    else:
        details_text = u'Студент був відредагований'

    s_id = u'id студента: %s' % (kwargs['instance'].id or None)
    s_name = u'Повне ім’я студента: %s %s' % ((kwargs['instance'].first_name or None),
        (kwargs['instance'].last_name or None))

    logging.info( '%s, %s, %s' % (details_text, s_id, s_name))