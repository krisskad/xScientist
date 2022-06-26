from django.shortcuts import render
import random
from homepage.models import *
import requests


def index(request):
    ################## company ####################
    company = Company.objects.all().order_by("created_date")[0]

    ################## our work ####################
    our_work = OurWork.objects.all().order_by("created_date")

    ################## our team ####################
    technology = Technology.objects.all().order_by("created_date")

    ################## our team ####################
    our_team = OurTeam.objects.all().order_by("created_date")

    ################## response ####################
    context = {
        "team": our_team,
        "work": our_work,
        "company":company,
        "technology":technology
    }
    return render(request, 'homepage/index.html', context)