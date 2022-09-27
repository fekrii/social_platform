from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # _auth app urls
    path('auth/', include('_auth.urls')),
    path('posts/', include('post.urls')),

]
