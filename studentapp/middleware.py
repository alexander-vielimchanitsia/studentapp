# -*- coding: utf-8 -*-

from django.db import connection
from time import time
from operator import add
import re


class StatsMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        n = len(connection.queries)

        start = time()
        response = view_func(request, *view_args, **view_kwargs)
        tot_time = time() - start
        db_queries = len(connection.queries) - n
        if db_queries:
            db_time = reduce(add, [float(q['time'])
                                   for q in connection.queries[n:]])
        else:
            db_time = 0.0

        # and backout python time
        python_time = tot_time - db_time

        response.content = response.content.replace('<body>',
            '<body>Весь час генерації сторінки: %.2f, '
            'Python: %.2f, DB: %.2f, Всього запитів: %.d'
            % (tot_time, tot_time, db_time, db_queries))
        return response