from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from soapdishapi.models import Oil
from soapdishapi.serializers import OilSerializer


class OilView(ViewSet):
    """Oil ViewSet"""

    def list(self, request):
        """Handle GET requests to get all oils

        Returns:
            Response -- JSON serialized list of recipes
        """
        oils = Oil.objects.all()
        serializer = OilSerializer(oils, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single oil

        Returns:
            Response -- JSON serialized oil
        """
        try:
            oil = Oil.objects.get(pk=pk)
            serializer = OilSerializer(oil, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Oil.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
