from django.template.loader import render_to_string

from MurrCard.models import Murr


def show_categories(request):
    is_search = '/murrs/' in request.path
    is_murr_list = request.path == '/murrs/'
    is_murrs_by_categories = '/murrs/by_category/' in request.path

    if not any([is_search, is_murr_list, is_murrs_by_categories]):
        return {}

    # context = {'categories': Murr.CATEGORIES}
    context = {'tip': 'test'}
    tip_data = render_to_string(
        'categories.html',  # можно подставлять любой фрагмент кода .html
        # и отрисовывать только в нужном месте или на нужной странице
        context)
    return {'tip_data': tip_data}
