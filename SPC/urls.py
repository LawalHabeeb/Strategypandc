from django.urls import path
from . import views

app_name = "SPC"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("accounting", views.accounting, name="accounting"),
    path("finance", views.finance, name="finance"),
    path("ita", views.ita, name="ita"),
    path("risk", views.risk, name="risk"),
    path("tax", views.tax, name="tax"),
    path("training", views.train, name="training"),
    path("contact", views.contact, name="contact"),
    path("insights", views.insight_view, name="insights"),
    path("<slug:slug>/<int:id>/", views.insight_detail, name="insight_detail"),
]
