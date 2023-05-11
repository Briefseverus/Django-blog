from django.contrib import admin


from .models import pro




class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'language', 'link']
    list_filter = ['language']
    search_fields = ['title']


admin.site.register(pro, PostAdmin)
