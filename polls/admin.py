from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question text", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

class ChoiceTest(admin.ModelAdmin):
    fieldsets = [
        ("Question Selection", {"fields": ["question"]}),
        ("Choice Information", {"fields": ["choice_text"],}),
        (None, {"fields": ["votes"]}),
    ]

    
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceTest)
