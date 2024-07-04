from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(ResumeHeader)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("resume_name_uk","resume_name_en", 
                    "is_active", "profile_uk","profile_en", 
                    "full_name_uk", "full_name_en")
    list_display_links = ("resume_name_uk","resume_name_en",
                          "profile_uk","profile_en", "full_name_uk", 
                          "full_name_en")
    list_editable = ("is_active",)


admin.site.register(ContactItem)

@admin.register(TittlePhoto)
class TittlePhotoAdmin(admin.ModelAdmin):
    list_display = ("get_photo_hmtl",  "is_active")
    list_editable = ("is_active",)
    readonly_fields = ("get_photo_hmtl", )
    def get_photo_hmtl(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

@admin.register(SkillItem)
class SkillItemAdmin(admin.ModelAdmin):
    list_display = ("text_uk","text_en")
    list_display_links = ("text_uk","text_en")

@admin.register(KnowledgeItem)
class KnowledgeItemAdmin(admin.ModelAdmin):
    list_display = ("text_uk","text_en")
    list_display_links = ("text_uk","text_en")

@admin.register(EmloymentHistoryItem)
class EmloymentHistoryItemAdmin(admin.ModelAdmin):
    list_display = ("firm_name_uk","firm_name_en", "position_name_uk",
                    "position_name_en", "text_uk","text_en")
    list_display_links = ("firm_name_uk","firm_name_en", "position_name_uk",
                          "position_name_en", "text_uk","text_en")
    
@admin.register(HobbyItem)
class HobbyItemAdmin(admin.ModelAdmin):
    list_display = ("text_uk","text_en")
    list_display_links = ("text_uk","text_en")