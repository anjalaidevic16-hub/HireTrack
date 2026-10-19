from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import ApplicationForm, CompanyForm, RegisterForm
from .models import Application, Company

def register_view(request):
 if request.user.is_authenticated: return redirect("dashboard")
 form=RegisterForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  user=form.save(); login(request,user); messages.success(request,"Your account is ready."); return redirect("dashboard")
 return render(request,"applications/register.html",{"form":form})

def login_view(request):
 if request.user.is_authenticated: return redirect("dashboard")
 form=AuthenticationForm(request,data=request.POST or None)
 if request.method=="POST" and form.is_valid():
  login(request,form.get_user()); return redirect("dashboard")
 return render(request,"applications/login.html",{"form":form})

@login_required
def logout_view(request):
 if request.method=="POST": logout(request); return redirect("login")
 return redirect("dashboard")

@login_required
def dashboard(request):
 apps=Application.objects.filter(owner=request.user)
 counts={x["status"]:x["total"] for x in apps.values("status").annotate(total=Count("id"))}
 return render(request,"applications/dashboard.html",{"total_count":apps.count(),"interview_count":counts.get("Interview",0),"offer_count":counts.get("Offer",0),"rejected_count":counts.get("Rejected",0),"recent_apps":apps.select_related("company")[:5],"company_count":Company.objects.filter(owner=request.user).count()})

@login_required
def applications_view(request):
 qs=Application.objects.filter(owner=request.user).select_related("company")
 search=request.GET.get("q","").strip(); status=request.GET.get("status","")
 if search: qs=qs.filter(Q(role__icontains=search)|Q(company__name__icontains=search))
 if status in Application.Status.values: qs=qs.filter(status=status)
 return render(request,"applications/applications.html",{"applications":qs,"search":search,"selected_status":status,"statuses":Application.Status.choices})

@login_required
def application_add(request):
 form=ApplicationForm(request.POST or None); form.fields["company"].queryset=Company.objects.filter(owner=request.user)
 if request.method=="POST" and form.is_valid():
  item=form.save(commit=False); item.owner=request.user; item.save(); messages.success(request,"Application added."); return redirect("applications")
 return render(request,"applications/application_form.html",{"form":form,"page_title":"Add application"})

@login_required
def application_edit(request,pk):
 item=get_object_or_404(Application,pk=pk,owner=request.user)
 form=ApplicationForm(request.POST or None,instance=item); form.fields["company"].queryset=Company.objects.filter(owner=request.user)
 if request.method=="POST" and form.is_valid():
  form.save(); messages.success(request,"Application updated."); return redirect("applications")
 return render(request,"applications/application_form.html",{"form":form,"page_title":"Edit application"})

@login_required
@require_POST
def application_delete(request,pk):
 get_object_or_404(Application,pk=pk,owner=request.user).delete(); messages.success(request,"Application deleted."); return redirect("applications")

@login_required
def companies_view(request):
 return render(request,"applications/companies.html",{"companies":Company.objects.filter(owner=request.user),"form":CompanyForm()})

@login_required
def company_add(request):
 form=CompanyForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  company=form.save(commit=False); company.owner=request.user
  try: company.save()
  except Exception: form.add_error("name","You have already added a company with this name.")
  else: messages.success(request,"Company added."); return redirect("companies")
 return render(request,"applications/companies.html",{"companies":Company.objects.filter(owner=request.user),"form":form})

@login_required
@require_POST
def company_delete(request,pk):
 get_object_or_404(Company,pk=pk,owner=request.user).delete(); messages.success(request,"Company deleted along with its linked applications."); return redirect("companies")
