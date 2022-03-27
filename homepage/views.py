from django.shortcuts import render
import random
from homepage.models import *
import requests


def index(request):

    ################## hero image ####################

    images = list(HeroImage.objects.all().values_list("image_url", flat=True))

    if len(images)>0:
        url = random.choice(images)
        if not "http" in url:
            images = list(HeroImage.objects.all().values_list("image_source", flat=True))
            url = random.choice(images)


    ################## slogan ####################
    slogan_list = list(Slogan.objects.all().values_list("text", flat=True))

    if len(slogan_list)>0:
        slogan = random.choice(slogan_list)
    else:
        slogan = "START YOUR JOURNEY WITH US AS A "

    type_effect = ["xSCIENTIST", "xENGINEER", "xCREATOR"]
    # slogan_split = slogan.split(" ")
    # slogan_underline = slogan_split[-1]
    # slogan_split.remove(slogan_underline)
    # slogan = " ".join(slogan_split).upper()

    slogan = {
        "slogan":slogan,
        # "slogan_underline":slogan_underline,
        "type_effect":type_effect
    }

    ################## quote ####################

    try:
        response = requests.request("GET", url="https://type.fit/api/quotes")

        if response.status_code == 200:
            while True:
                quote = random.choice(response.json())
                if len(quote["text"])<110 and quote["author"]:
                    break
    except:
        quote = ""

    ################## What we are offering ####################
    feature = list(Feature.objects.all().values_list("title", flat=True))
    if len(feature)<1:
        feature = ""
    else:
        feature = feature[0]

    ################## response ####################
    context = {
        "hero_image": url,
        "slogan":slogan,
        "quote":quote,
        "feature_desc":feature
    }
    return render(request, 'homepage/index.html', context)