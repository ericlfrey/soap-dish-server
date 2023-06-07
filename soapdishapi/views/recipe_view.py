"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from soapdishapi.models import Recipe, RecipeOil, Soaper, Oil


class RecipeView(ViewSet):
    """Level up game types view"""

    def list(self, request):
        """Handle GET requests to get all recipes

        Returns:
            Response -- JSON serialized list of recipes
        """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single recipe

        Returns:
            Response -- JSON serialized recipe
        """
        try:
            recipe = Recipe.objects.get(pk=pk)
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
        oils = request.data['oils']
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

        recipe = Recipe.objects.get(pk=pk)
        recipe.title = request.data["title"]
        recipe.water_amount = request.data["water_amount"]
        recipe.lye_amount = request.data["lye_amount"]
        recipe.super_fat = request.data["super_fat"]
        recipe.description = request.data["description"]
        recipe.notes = request.data["notes"]
        recipe.public = request.data["public"]
        recipe.save()

        recipe_oils = request.data["oils"]

        recipe_oil_list = []
        for oil in recipe_oils:
            if 'id' in oil:
                oil_obj = RecipeOil.objects.get(pk=oil["id"])
                recipe_oil_list.append(oil_obj)

        current_oils = RecipeOil.objects.all().filter(recipe=recipe)
        for current_oil in current_oils:
            if current_oil not in recipe_oil_list:
                current_oil.delete()

        for recipe_oil in recipe_oils:
            if 'id' in recipe_oil:
                updated_oil = RecipeOil.objects.get(pk=recipe_oil["id"])
                updated_oil.oil = Oil.objects.get(pk=recipe_oil["oilId"])
                updated_oil.amount = recipe_oil['amount']
                updated_oil.save()
            else:
                RecipeOil.objects.create(
                    recipe=recipe,
                    oil=Oil.objects.get(pk=recipe_oil["oilId"]),
                    amount=recipe_oil["amount"]
                )

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipes"""
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'water_amount',
            'lye_amount',
            'super_fat',
            'description',
            'notes',
            'public'
        )


class OilSerializer(serializers.ModelSerializer):
    """Doc"""

    class Meta:
        model = RecipeOil
        fields = (
            'id',
            'amount',
            'oil_name'
        )


class SingleRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipes"""

    recipe_oils = OilSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'maker',
            'title',
            'water_amount',
            'lye_amount',
            'super_fat',
            'description',
            'notes',
            'public',
            'recipe_oils'
        )


class CreateRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for creating a new Recipe instance"""
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'water_amount',
            'lye_amount',
            'super_fat',
            'description',
            'notes',
            'public'
        )
