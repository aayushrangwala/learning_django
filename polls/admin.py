from django.contrib import admin
from polls.models import Question,Choice

#in this below class the admin.StackedInline
#means to model an objeect of a class


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# by default value of extra is 0 whhich represents the no. of times
# of the object above

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','date')
    #list_display is the pre-defined object which figures the display of question listS
    fieldsets = [
       ('Question',{'fields':['question_text']}),
       ('Date Information', {'fields':['date'], 'classes':['collapse']}),
       ]
    
    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_filter = ['date']
   # fields = ['date','question_text']

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)


