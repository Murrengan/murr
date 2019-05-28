from django.template.loader import render_to_string

from MurrCard.models import Murr


def show_categories(request):
    is_search = '/murrs/' in request.path
    is_murr_list = request.path == '/murrs/'
    is_murrs_by_categories = '/murrs/murrs_by_category/' in request.path

    if not any([is_search, is_murr_list, is_murrs_by_categories]):
        return {}

    context = {'categories': Murr.CATEGORIES}
    categories_bar = render_to_string('categories.html', context)
    return {'categories_bar': categories_bar}
