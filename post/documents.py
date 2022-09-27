from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import BasePost, TravelPost


@registry.register_document
class BasePostDocument(Document):



    class Index:
        name = 'basepost'

    class Django:
        model = BasePost
        fields = [
            'id',
            'title'
        ]


@registry.register_document
class TravelPostDocument(Document):


    class Index:
        name = 'travelpost'

    class Django:
        model = TravelPost
        fields = [
            'content',
            'destinationCountry'
        ]