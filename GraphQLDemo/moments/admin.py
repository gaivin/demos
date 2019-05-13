from django.contrib import admin

# Register your models here.
from moments.models import User, Post


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'gender', 'age')
    search_fields = ('first_name', 'last_name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time')
    search_fields = ('title',)


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)