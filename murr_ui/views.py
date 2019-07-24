from django.shortcuts import render


def murr_ui(request):
    return render(request, 'murr_ui/murr_ui.html')
