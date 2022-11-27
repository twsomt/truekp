from django.contrib import admin
from home.models import Feed

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'content'

    )