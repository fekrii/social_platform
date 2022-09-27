from elasticsearch_dsl import Q, Search
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from _auth.models import CustomUser
from post.documents import BasePostDocument
from post.models import BasePost, TravelPost, NewsPost, EventPost, PostViews
from post.serializers import BasePostSerializer, TravelPostSerializer, NewsPostSerializer, EventPostSerializer


class PostCreate(APIView):

    def post(self, request):
        try:
            user_obj = CustomUser.objects.get(id=request.user.id)
        except:
            return Response({
                'success': False,
                'data': None,
                'message': 'Invalid User!'
            }, status.HTTP_400_BAD_REQUEST)
        try:
            # using pop to get post_type and delete it from request.data at the same time
            # TODO: ue post_type as parameter in the url
            post_type = request.data.pop('post_type')
            if post_type == "travel":
                travel_obj = TravelPost.objects.create(created_by=user_obj, **request.data)
                serializer = TravelPostSerializer(travel_obj)

            elif post_type == "news":
                news_obj = NewsPost.objects.create(created_by=user_obj, **request.data)
                serializer = NewsPostSerializer(news_obj)

            elif post_type == "event":
                event_obj = EventPost.objects.create(created_by=user_obj, **request.data)
                serializer = EventPostSerializer(event_obj)
            else:
                return Response({
                    'success': False,
                    'data': None,
                    'message': 'post type must be provided'
                })
            return Response({
                'success': True,
                'data': serializer.data,
                'message': 'Post created successfully!'
            })
        except:
            return Response({
                'success': True,
                'data': None,
                'message': 'Post not created check data provided'
            })


# Get all posts
class PostsList(generics.ListAPIView):
    queryset = BasePost.objects.all()
    serializer_class = BasePostSerializer


# Get posts created by Me using Token
class MyPostsList(generics.ListAPIView):
    queryset = BasePost.objects.all()
    serializer_class = BasePostSerializer

    def get_queryset(self, *args, **kwargs):
        # user = CustomUser.objects.gte()
        post = super().get_queryset(*args, **kwargs).filter(
            created_by=self.request.user

        )
        return post



class SearchPosts(APIView, LimitOffsetPagination):
    base_post_erializer = BasePostSerializer
    search_document = BasePostDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'title'
                ]
            )
            search = self.search_document.search().query(q)
            response = search.execute()

            serializer = self.base_post_erializer(response, many=True)
            return Response({
                'success': True,
                'data': serializer.data,
                'message': "search data found"
            })

        except Exception as e:
            return Response({
                'success': False,
                'data': None,
                'message': "can't retrieve search data"
            })


class PostAddView(APIView):
    def get(self, request, post_id):
        add_view = PostViews.objects.get_or_create(user=request.user, post_id=post_id)
        return Response({
            'success': True,
            'data': None,
            'message': "you have viewed this post"
        })
