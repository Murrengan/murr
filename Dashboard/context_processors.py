from MurrCard.models import Murr


def show_categories(request):
    categories = Murr.CATEGORIES
    context = {
        'categories': categories
    }

    return context
