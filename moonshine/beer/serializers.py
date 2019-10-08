from rest_framework import fields, serializers
from beer.models import BeerModel


class BeerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeerModel

        fields = (
            'name',
            'beer_type',
            'description',
        )
