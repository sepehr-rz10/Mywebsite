from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    emty_value_display = '-emty-'
    #fields = ('title' ,)
    list_display = ('title' , 'counted_views' , 'status' , 'published_date' , 'created_date')
    list_filter = ('status' ,)
    #ordering = ['-created_date']
    search_fields = ['title' , 'content']

#admin.site.register(Post , PostAdmin)