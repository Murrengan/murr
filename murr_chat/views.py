from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/signup/')
def murr_chat(request):
    return render(request, 'murr_chat/murr_chat.html')
