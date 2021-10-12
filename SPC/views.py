from django.http.response import BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages


from SPC.forms import ContactForm
from .models import Insight, Team

# Create your views here.


def index(request):
    insight = Insight.objects.all()
    context = {
        "page_title": "WELCOME TO SPC",
        "insights": insight,
    }
    return render(request, "SPC/index.html", context)

def about(request):
    team = Team.objects.all()
    context = {
        "page_title": "About SPC",
        "teams": team,
    }
    return render(request, "SPC/about.html", context)

def services(request):
    context = {"page_title": "Our Services"}
    return render(request, "SPC/services.html", context)

def accounting(request):
    context = {"page_title": "Accounting and Assurance"}
    return render(request, "SPC/accandass.html", context)

def finance(request):
    context = {"page_title": "Financial Advisory"}
    return render(request, "SPC/fin.html", context)

def ita(request):
    context = {"page_title": "Information Technology Advisory"}
    return render(request, "SPC/ita.html", context)

def risk(request):
    context = {"page_title": "Risk Advisory"}
    return render(request, "SPC/risk.html", context)

def tax(request):
    context = {"page_title": "Tax Advisory"}
    return render(request, "SPC/tax.html", context)

def train(request):
    context = {"page_title": "Training Services"}
    return render(request, "SPC/training.html", context)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            subject = 'Website Inquiry'
            body = {
                'full_name': contact_form.cleaned_data['full_name'],
                'email': contact_form.cleaned_data['email_address'],
                'company_name': contact_form.cleaned_data['company_name'],
                'message': contact_form.cleaned_data['message'],
            }

            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'strategypandc@outlook.com', ['strategypandc@outlook.com'])
                messages.success(request, "message successfully sent")
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            
            return redirect("SPC:contact")
        else:
            messages.error(request, "Please Resend Message")
    else:
        contact_form = ContactForm()
    
    context = {
        "page_title": "Contact Us",
        "contact_form": contact_form,
        }
    return render(request, "SPC/contact.html", context)

def insights(request):
    context ={"page_title": "Insights"}
    return render(request, "SPC/insights.html", context)

def insight_detail(request, slug, id):
    insight = Insight.objects.get(slug=slug, id=id)
    context = {"insight": insight}
    return render(request, "SPC/insight_detail.html", context)