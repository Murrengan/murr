from MurrCard.models import Category, Murr


def show_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return context
