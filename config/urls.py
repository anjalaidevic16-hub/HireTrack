
from django.contrib import admin
from django.urls import path
from applications import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("admin/", admin.site.urls),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("applications/", views.applications_view, name="applications"),
    path("applications/add/", views.application_add, name="application_add"),
    path(
        "applications/<int:pk>/edit/",
        views.application_edit,
        name="application_edit",
    ),
    path(
        "applications/<int:pk>/delete/",
        views.application_delete,
        name="application_delete",
    ),

    path("companies/", views.companies_view, name="companies"),
    path("companies/add/", views.company_add, name="company_add"),
    path(
        "companies/<int:pk>/delete/",
        views.company_delete,
        name="company_delete",
    ),
]
