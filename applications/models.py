from django.conf import settings
from django.db import models
class Company(models.Model):
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="companies")
 name=models.CharField(max_length=160)
 website=models.URLField(blank=True)
 location=models.CharField(max_length=160,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["name"]
  constraints=[models.UniqueConstraint(fields=["owner","name"],name="unique_company_per_owner")]
 def __str__(self): return self.name
class Application(models.Model):
 class Status(models.TextChoices):
  SAVED="Saved","Saved"; APPLIED="Applied","Applied"; INTERVIEW="Interview","Interview"; OFFER="Offer","Offer"; REJECTED="Rejected","Rejected"
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="job_applications")
 company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="applications")
 role=models.CharField(max_length=160)
 applied_on=models.DateField(null=True,blank=True)
 status=models.CharField(max_length=20,choices=Status.choices,default=Status.SAVED)
 job_url=models.URLField(blank=True)
 notes=models.TextField(blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta: ordering=["-created_at"]
 def __str__(self): return f"{self.role} at {self.company.name}"
