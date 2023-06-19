"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from soapdishapi.models import Recipe, Comment, Soaper, RecipeComment
from soapdishapi.serializers import CommentSerializer


class CommentView(ViewSet):
    """Recipe Viewset"""

    # def list(self, request):
    #     """Handle GET requests to get all comments

    #     Returns:
    #         Response -- JSON serialized list of comments
    #     """

    #     # recipes = Recipe.objects.annotate(
    #     #     is_favorite=Count('favorites'), filter=Q(favorites=user)).filter(maker=user)
    #     serializer = RecipeSerializer(recipes, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        # soaper = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized Comment instance
        """
        soaper = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        recipe = Recipe.objects.get(pk=request.data["recipeId"])
        comment = Comment.objects.create(
            soaper=soaper,
            text=request.data["text"],
            date_added=request.data["dateAdded"]
        )
        serializer = CommentSerializer(comment, many=False)

        RecipeComment.objects.create(
            recipe=recipe,
            comment=comment
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.text = request.data["text"]
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handle DELETE requests for a single comment"""
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
