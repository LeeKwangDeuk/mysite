from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# 1
# admin.site.register(Question)
# admin.site.register(Choice)

# 2
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 1
    # fields = ["pub_date", "question_text"]

    # 2
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    inlines = [ChoiceInline]

    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
