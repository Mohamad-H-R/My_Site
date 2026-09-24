from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    search_fields = ['title', 'message']    
    list_filter = ('email',)

admin.site.register(Contact,ContactAdmin)