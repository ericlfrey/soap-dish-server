from rest_framework import serializers
from soapdishapi.models import Recipe, RecipeOil


class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipes"""

    is_favorite = serializers.BooleanField(required=False)

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
            'is_favorite'
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
    is_favorite = serializers.BooleanField(required=False)

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
            'recipe_oils',
            'is_favorite'
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