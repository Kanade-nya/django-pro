from django.contrib import admin

# Register your models here.

from .models import Question,Choice

class ChoiceInline(admin.TabularInline): # StackedInline 和 TabularInline 区别差不多
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): # 创建模型后台类
    # fields = ['pub_date','question_text']
    # 进阶方法
    fieldsets = [
        (None, {'fields': ['pub_date']}),
        ("More Information", { 'fields' : ['question_text']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin) # 配置在admin索引页中
admin.site.register(Choice)