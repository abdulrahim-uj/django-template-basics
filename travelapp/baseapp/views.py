from django.shortcuts import render
from . models import ChooseUs, OurTeam


def index(request):
    chooseus = ChooseUs.objects.all()
    ourteam = OurTeam.objects.all()
    context = {
        'project_name': "Travel App",
        'title': "Home",
        'chooses': chooseus,
        'teams': ourteam,
    }
    return render(request, "baseapp/index.html", context=context)
