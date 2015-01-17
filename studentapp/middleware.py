# -*- coding: utf-8 -*-

from time import time


class StatsMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        start = time()
        response = view_func(request, *view_args, **view_kwargs)
        totTime = time() - start

        response.content = response.content.replace('<body>', '<body>Час генерації сторінки: %.2f' % totTime)

        return response