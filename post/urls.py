
from django.urls import path
from post.views import PostsList, MyPostsList, PostCreate, SearchPosts, PostAddView

app_name = "post"


urlpatterns = [
    path('', PostCreate.as_view()),
    path('all/', PostsList.as_view()),
    path('my/', MyPostsList.as_view()),
    path('search/<str:query>', SearchPosts.as_view()),
    path('details/<int:post_id>', PostAddView.as_view()),
]
