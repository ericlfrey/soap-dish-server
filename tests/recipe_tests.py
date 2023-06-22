import json
from rest_framework import status
from rest_framework.test import APITestCase
from soapdishapi.models import Soaper, Recipe, RecipeOil

data = {
    "title": "Test Recipe",
    "water_amount": 2.1,
    "lye_amount": 3.2,
    "super_fat": 0.05,
    "description": "Test Description",
    "notes": "Test Notes",
    "public": True,
    "oilList": [
        {
            "oilId": 42,
            "amount": 10
        },
        {
            "oilId": 4,
            "amount": 23
        }
    ]
}


class RecipeTests(APITestCase):

    # access the fixtures
    fixtures = ['soapers', 'recipes', 'oils', 'recipe_oils']

    def setUp(self):
        self.soaper = Soaper.objects.first()
        self.client.credentials(HTTP_AUTHORIZATION=self.soaper.uid)

    def test_get_all_recipes(self):
        """Ensure we can retrieve all recipes."""
        response = self.client.get("/recipes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_recipe(self):
        """
        Ensure we can create a new recipe.
        """
        # Define the endpoint in the API to which the request will be sent
        url = "/recipes"

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the recipe was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(
            json_response,
            {
                "id": json_response["id"],
                "title": "Test Recipe",
                "water_amount": "2.100",
                "lye_amount": "3.200",
                "super_fat": "0.050",
                "description": "Test Description",
                "notes": "Test Notes",
                "public": True,
            }
        )

    def test_get_recipe(self):
        """
        Ensure we can get an existing recipe.
        """
        soaper = Soaper.objects.first()
        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.public = data["public"]
        recipe.save()

        for oil in data["oilList"]:
            RecipeOil.objects.create(
                recipe=recipe,
                oil_id=oil["oilId"],
                amount=oil["amount"]
            )

        response = self.client.get(f"/recipes/{recipe.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json_response,
            {
                "id": json_response["id"],
                "maker": 1,
                "title": "Test Recipe",
                "water_amount": "2.100",
                "lye_amount": "3.200",
                "super_fat": "0.050",
                "description": "Test Description",
                "notes": "Test Notes",
                "public": True,
                'recipe_oils': [
                    {
                        'amount': '10.000',
                        'id': 7,
                        'oil': {
                            'id': 42,
                            'name': 'Shea Butter',
                            'sap': '0.133'
                        }
                    },
                    {
                        'amount': '23.000',
                        'id': 8,
                        'oil': {
                            'id': 4,
                            'name': 'Avocado Butter',
                            'sap': '0.133'
                        }
                    }
                ],
                "comments": [],
                "is_favorite": False
            }
        )

    def test_change_recipe(self):
        """
        Ensure we can change an existing recipe.
        """
        soaper = Soaper.objects.first()
        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.public = data["public"]
        recipe.save()

        # DEFINE NEW PROPERTIES FOR Recipe
        updated_payload = {
            "title": "new title",
            "waterAmount": 2.22,
            "lyeAmount": 3.33,
            "superFat": 0.06,
            "description": "new description",
            "notes": "new notes",
            "public": False,
            "oilList": [
                {
                    "oilId": 42,
                    "amount": 10
                },
                {
                    "oilId": 4,
                    "amount": 23
                }
            ]
        }

        response = self.client.put(
            f"/recipes/{recipe.id}", updated_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET recipe again to verify changes were made
        response = self.client.get(f"/recipes/{recipe.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json_response,
            {
                'id': 4,
                'maker': 1,
                'title': 'new title',
                'water_amount': '2.220',
                'lye_amount': '3.330',
                'super_fat': '0.060',
                'description': 'new description',
                'notes': 'new notes',
                'public': False,
                'recipe_oils': [
                    {
                        'id': 7,
                        'oil': {
                            'id': 42,
                            'name': 'Shea Butter',
                            'sap': '0.133'
                        },
                        'amount': '10.000'
                    },
                    {
                        'id': 8,
                        'oil': {
                            'id': 4,
                            'name': 'Avocado Butter',
                            'sap': '0.133'
                        },
                        'amount': '23.000'
                    }
                ],
                'comments': [],
                'is_favorite': False
            }
        )

    def test_delete_recipe(self):
        """
        Ensure we can delete an existing recipe.
        """
        soaper = Soaper.objects.first()
        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.public = data["public"]
        recipe.save()

        # DELETE the recipe you just created
        response = self.client.delete(f"/recipes/{recipe.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the recipe again to verify you get a 404 response
        response = self.client.get(f"/recipes/{recipe.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_user_recipes(self):
        """Ensure we can get all recipes for a user"""
        soaper = Soaper()
        soaper.uid = "1234567890"
        soaper.first_name = "Test"
        soaper.last_name = "User"
        soaper.save()

        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.public = data["public"]
        recipe.save()

        all_recipes = Recipe.objects.all()
        user_recipes = Recipe.objects.all().filter(maker=soaper.id)
        soapers = Soaper.objects.all()
        self.assertFalse(len(all_recipes) == len(user_recipes))
        self.assertEqual(len(user_recipes), 1)
        self.assertEqual(len(soapers), 2)

    def test_get_all_public_recipes(self):
        """Ensure we can get all public recipes"""
        soaper = Soaper.objects.first()
        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.public = False
        recipe.save()

        all_recipes = Recipe.objects.all()
        public_recipes = Recipe.objects.all().filter(public=True)
        private_recipes = Recipe.objects.all().filter(public=False)
        self.assertFalse(len(all_recipes) == len(public_recipes))
        self.assertEqual(len(private_recipes), 1)

    def test_favorites(self):
        """Ensure we can get all favorite recipes"""
        # Create a new recipe
        soaper = Soaper.objects.first()
        recipe = Recipe()
        recipe.maker = soaper
        recipe.title = data["title"]
        recipe.water_amount = data["water_amount"]
        recipe.lye_amount = data["lye_amount"]
        recipe.super_fat = data["super_fat"]
        recipe.description = data["description"]
        recipe.notes = data["notes"]
        recipe.save()

        # Add the recipe to the favorites list
        recipe.favorites.add(soaper)
        # Get all recipes and all favorite recipes
        all_recipes = Recipe.objects.all()
        favorite_recipes = Recipe.objects.all().filter(favorites=soaper)
        # Assert that the lists are not the same length
        self.assertFalse(len(all_recipes) == len(favorite_recipes))
        # Assert that the recipe is in the favorites list
        self.assertEqual(len(favorite_recipes), 1)

        # Assert that response is 200
        response = self.client.get("/recipes/favorites")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Remove the recipe from the favorites list
        recipe.favorites.remove(soaper)
        favorite_recipes = Recipe.objects.all().filter(favorites=soaper)
        # Assert that the recipe is not in the favorites list
        self.assertFalse(len(favorite_recipes), 0)
