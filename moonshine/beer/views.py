from django.http import HttpResponse
from rest_framework import status, views
from rest_framework.response import Response

from beer.models import BeerModel
from beer.serializers import BeerModelSerializer


class BeerView(views.APIView):
    serializer_class = BeerModelSerializer

    def get(self, request, pk=None):
        """
            Method:             GET
            Url:                /api/beer/pk/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    beer.object.dict
                                }
        """
        try:
            beer = BeerModel.objects.get(id=pk)
            beer_serializer = self.serializer_class(beer)

            return Response(
                beer_serializer.data,
                status=status.HTTP_200_OK)

        except Exception as ex:

            return Response(
                {'message': str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, **kwargs):

        try:
            BeerModel.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                beer_type=request.POST.get('beer_type'))

            return HttpResponse(status=201)

        except Exception as ex:

            return Response(
                {'message': str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
