"""View module for handling requests about Comments"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from soapdishapi.models import Recipe, RecipeOil, Soaper, Oil
from soapdishapi.serializers import RecipeSerializer, SingleRecipeSerializer, CreateRecipeSerializer


class RecipeView(ViewSet):
    """Recipe Viewset"""

    def list(self, request):
        """Handle GET requests to get all recipes

        Returns:
            Response -- JSON serialized list of recipes
        """
        user = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        recipes = Recipe.objects.annotate(
            is_favorite=Count('favorites', filter=Q(favorites=user))).filter(maker=user)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single recipe

        Returns:
            Response -- JSON serialized recipe
        """
        user = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        try:
            recipe = Recipe.objects.annotate(
                is_favorite=Count('favorites', filter=Q(favorites=user))).get(pk=pk)
            serializer = SingleRecipeSerializer(recipe, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized recipe instance
        """
        maker = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        serializer = CreateRecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(maker=maker)

        # Create a RecipeOil Instance for every oil in the oil list
        oils = request.data['oilList']
        for oil in oils:
            recipe = Recipe.objects.get(pk=serializer.data['id'])
            oil_obj = Oil.objects.get(pk=oil["oilId"])
            RecipeOil.objects.create(
                recipe=recipe,
                oil=oil_obj,
                amount=oil["amount"]
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a recipe

        Returns:
            Response -- Empty body with 204 status code
        """

        try:
            recipe = Recipe.objects.get(pk=pk)
            recipe.title = request.data["title"]
            recipe.water_amount = request.data["waterAmount"]
            recipe.lye_amount = request.data["lyeAmount"]
            recipe.super_fat = request.data["superFat"]
            recipe.description = request.data["description"]
            recipe.notes = request.data["notes"]
            recipe.public = request.data["public"]
            recipe.save()

            # Delete all current RecipeOil instances for the recipe
            current_oils = RecipeOil.objects.filter(recipe=recipe)
            for oil in current_oils:
                oil.delete()

            # Create a RecipeOil Instance for every oil in the oil list
            recipe_oils = request.data["oilList"]
            for recipe_oil in recipe_oils:
                try:
                    RecipeOil.objects.create(
                        recipe=recipe,
                        oil=Oil.objects.get(pk=recipe_oil["oilId"]),
                        amount=recipe_oil["amount"]
                    )
                except Oil.DoesNotExist:
                    # Handle the case when the specified Oil doesn't exist
                    return Response("Oil not found", status=status.HTTP_404_NOT_FOUND)

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        except Recipe.DoesNotExist:
            # Handle the case when the specified Recipe doesn't exist
            return Response("Recipe not found", status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            # Handle the case when a required field is missing from the request data
            return Response(f"Missing field: {str(e)}", status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle any other unexpected exceptions
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """ Handle DELETE requests for a single recipe"""
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
        """Post request for a user to favorite a recipe"""

        user = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        recipe = Recipe.objects.get(pk=pk)
        recipe.favorites.add(user)
        return Response({'message': 'Recipe favorited'}, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
        """Delete request for a user to unfavorite a recipe"""

        user = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        recipe = Recipe.objects.get(pk=pk)
        recipe.favorites.remove(user)
        return Response({'message': 'Recipe unfavorited'}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def favorites(self, request):
        """Get the user's liked products"""
        user = Soaper.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        favorite_recipes = Recipe.objects.filter(favorites=user)
        serializer = RecipeSerializer(favorite_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def public(self, request):
        """Get the user's liked products"""
        public_recipes = Recipe.objects.filter(public=True)
        serializer = RecipeSerializer(public_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
