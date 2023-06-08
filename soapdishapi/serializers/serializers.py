from rest_framework import serializers
from soapdishapi.models import Recipe, RecipeOil, Oil


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
        depth = 1


class RecipeOilSerializer(serializers.ModelSerializer):
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

    recipe_oils = RecipeOilSerializer(many=True)
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


class OilSerializer(serializers.ModelSerializer):
    """JSON serializer for oils"""

    class Meta:
        model = Oil
        fields = (
            'id',
            'name',
            'sap'
        )
