from django.db import models
from django.db.models.fields import related
from model_utils.managers import InheritanceManager
from _auth.models import CustomUser





class BasePost(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, related_name='%(class)s',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = InheritanceManager()

    # this property is to get a count of the post views
    @property
    def views_count(self):
        return PostViews.objects.filter(post=self).count()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.title)


class TravelPost(BasePost):
    content = models.TextField(max_length=255, blank=True, null=True)
    destinationCountry = models.CharField(max_length=255, blank=True, null=True)


class NewsPost(BasePost):
    content = models.TextField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)


class EventPost(BasePost):
    eventName = models.CharField(max_length=255, blank=True, null=True)
    eventStartTime = models.DateTimeField()
    eventLocation = models.CharField(max_length=255, blank=True, null=True)


class PostViews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(BasePost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.profile.firstName} liked {self.post.title}'