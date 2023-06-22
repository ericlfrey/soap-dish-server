from rest_framework import serializers
from soapdishapi.models import Recipe, RecipeOil, Oil, Comment


class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipes"""

    is_favorite = serializers.BooleanField(required=False)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'maker',
            'title',
            'description',
            'public',
            'is_favorite'
        )


class RecipeOilSerializer(serializers.ModelSerializer):
    """JSON serializer for recipe oils"""

    class Meta:
        model = RecipeOil
        fields = (
            'id',
            'oil',
            'amount',
        )
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""

    class Meta:
        model = Comment
        fields = (
            'id',
            'soaper',
            'recipe',
            'text',
            'date_added',
            'commenter_name'
        )


class SingleRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipes"""

    recipe_oils = RecipeOilSerializer(many=True)
    comments = CommentSerializer(many=True)
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
            'comments',
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
