from django.contrib import admin
from .models import *

class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 1

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    inlines = [FavoriteItemInline]

admin.site.register(UserProfile)
admin.site.register (Follow)
admin.site.register (Comment)
admin.site.register (CommentLike)
admin.site.register (Post)
admin.site.register (PostLike)
admin.site.register (Hashtag)
admin.site.register (PostContent)



