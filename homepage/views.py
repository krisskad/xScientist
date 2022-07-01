import os.path

from django.shortcuts import render
import random
from homepage.models import *
import requests
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from MAIN import settings
from django.template.loader import render_to_string


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


def send_email(request):
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    subject = f"xScientist | Message from {name}"
    body = f"{message} \n sent by : {from_email}"

    ##### save ######

    Message.objects.create(
        sender_name = name,
        sender_email = from_email,
        sender_message = message
    )

    if name and message and from_email:
        try:
            # send_mail(subject, body, settings.EMAIL_HOST_USER, ['krishna.g.kadam98500@gmail.com'])
            html_path = os.path.join(settings.BASE_DIR, "templates", "homepage", "welcome_email.html")
            msg_html = render_to_string(html_path, {'name': name})

            send_mail(
                subject = "xScientist",
                message= f"Hi {name}, \n\n Thank you for visiting and sharing your thoughts with us. \n\n Regards \n xScientist Tech LLP \n xscientist.in",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list = [from_email, ],
                html_message=msg_html
            )

        except BadHeaderError:
            return HttpResponseRedirect('home')
        return HttpResponseRedirect('home')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponseRedirect('home')