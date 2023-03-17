from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from cv.utils.query_debugger import query_debugger
from django.db.models import F
# Create your views here.

def cv(request):
    lang = request.GET.get('lang', "en")
    return render(request, "cv/cv.html", get_context(lang))

@query_debugger
def get_context(lang):
    
    headers = {
        "en":{"about": "About me", "skills": "Skills", "knowledge": "Knowledge and technologies", "work_history": "Work history (last three)"}, 
        "uk": {"about": "Про мене", "skills": "Досвід", "knowledge": "Знання та технології", "work_history": "Професійний досвід (останні 3 посади)"}}
    
    cv = ResumeHeader.objects.filter(pk=1).prefetch_related("contactitem_set", \
        "tittlephoto_set", "skillitem_set", "knowledgeitem_set", "emloymenthistoryitem_set")
    head = cv.values(full_name = F(f"full_name_{lang}"), resume_name = F(f"resume_name_{lang}"), \
        profile = F(f"profile_{lang}")).first()
    contact_items = cv.first().contactitem_set.all().values("text", "type")
    photo = cv.first().tittlephoto_set.all().first()
    skill_item = cv.first().skillitem_set.all().values(text = F(f"text_{lang}"))
    knowledge_item = cv.first().knowledgeitem_set.all().values(text = F(f"text_{lang}"))
    emloymenthistory_item = cv.first().emloymenthistoryitem_set.all().values(firm_name = F(f"firm_name_{lang}"), position_name = F(f"position_name_{lang}"), text = F(f"text_{lang}")) 
    
    return {
        "lang": lang,
        "headers": headers[lang],
        "head": head,
        "contact_items": contact_items,
        "photo": photo,
        "skill_item": skill_item,
        "knowledge_item": knowledge_item,
        "emloymenthistory_item": emloymenthistory_item,
        }