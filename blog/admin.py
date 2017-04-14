from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    fieldset = [
        ('Post', {'fields' : ['title', 'body']}),
        ('Date Information' ,{'fields' : ['date']}),
        ]
    search_fields = ['title']
    list_filter = ['date']

admin.site.register(Post,PostAdmin)
