from django.contrib import admin

from post.models import TravelPost, NewsPost, EventPost, BasePost, PostViews

@admin.register(BasePost)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(TravelPost)
class TravelPostAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    pass

@admin.register(EventPost)
class EventPostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostViews)
class PostViewsAdmin(admin.ModelAdmin):
    pass

