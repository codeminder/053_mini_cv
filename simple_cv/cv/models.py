from django.db import models

class BasePoint(models.Model):
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class ResumeHeader(BasePoint):

    resume_name_uk  = models.CharField(max_length=50, default="")
    resume_name_en  = models.CharField(max_length=50, default="")
    full_name_uk  = models.CharField(max_length=50, default="")
    full_name_en  = models.CharField(max_length=50, default="")
    profile_uk  = models.TextField(verbose_name="Про мене", default="", blank=True)
    profile_en  = models.TextField(verbose_name="About me", default="", blank=True)
    
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.resume_name_uk

class BaseCVPoint(BasePoint):
    
    cv_item = models.ManyToManyField(ResumeHeader, blank=True)
    order = models.IntegerField(verbose_name="Order")
    
    class Meta:
        abstract = True
        
class ContactItem(BaseCVPoint):
    
    PHONE = 'phone'
    EMAIL = 'email'
    VIBER = 'viber'
    TELEGRAM = "telegram"
    GITHUB = "github"
    LOCATION = "location"
    CHOICES = (
        (PHONE, 'Phone'),
        (EMAIL, 'E-mail'),
        (VIBER, 'Viber'),
        (TELEGRAM, 'Telegram'),
        (GITHUB, 'Github'),
        (LOCATION, 'Locations'),
    )
    text = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=25, choices=CHOICES, default=PHONE)
    
    class Meta():
        ordering = ["-order"]
    
    def __str__(self):
        return f"{self.type}-{self.text}"
    
class TittlePhoto(BaseCVPoint):
    
    photo    = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    class Meta:
        ordering = ["-order"]
    
class BaseItem(BaseCVPoint):
    
    text_uk = models.TextField(verbose_name="Опис", default="", blank=True)
    text_en = models.TextField(verbose_name="Description", default="", blank=True)
    
    
    class Meta:
        abstract = True

class SkillItem(BaseItem):
    
    class Meta:
        verbose_name = "Skill item"
        verbose_name_plural = "Skill item"
        ordering = ["-order"]
        
class KnowledgeItem(BaseItem):
    
    class Meta:
        verbose_name = "Knowledge item"
        verbose_name_plural = "Knowledge item"
        ordering = ["-order"]

class EmloymentHistoryItem(BaseItem):
    
    firm_name_uk = models.CharField(max_length=100, default="")
    firm_name_en = models.CharField(max_length=100, default="")
    position_name_uk = models.CharField(max_length=100, default="")
    position_name_en = models.CharField(max_length=100, default="")
    
    class Meta:
        verbose_name = "Employer history item"
        verbose_name_plural = "Employer history items"
        ordering = ["-order"]
        
        

