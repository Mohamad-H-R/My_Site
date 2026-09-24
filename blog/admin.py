from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','status','published_date','created_date')
    search_fields = ['title', 'content']
    list_filter = ('status',)
admin.site.register(Post,PostAdmin)
