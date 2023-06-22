# The Soap Dish -- Server Side!
This is the server side portion of my Nashville Software School Full Stack Capstone: [The Soap Dish](https://github.com/ericlfrey/soap-dish-client)

[Video Walkthrough](https://www.loom.com/share/25365a2897584b56932bf286f0173da8?sid=825496a2-3a9e-481a-a53e-1a911ceb1399)

![logo](https://user-images.githubusercontent.com/107942776/246680367-2b14c0d1-f0ad-451c-a60e-4792a6046e58.png)

## Topics
- [Overview](#overview)
- [MVP Features](#mvp-features)
- [Try the App Yourself](#try-the-app-yourself)
- [Planning The Soap Dish](#planning)
- [Code Snippets](#code-snippets)
- [Tech Stacks for TSD](#tech-stacks)
<!-- - [Stretch Features](#stretch-features) -->

## Overview
This is a Django server application built to provide the database for the [client-side app](https://github.com/ericlfrey/soap-dish-client)

The Soap Dish is a recipe creation app that allows a User to Create, Read, Update and Delete a Soapmaking Recipe, maintain notes and descriptions of the soap performance, and share the recipe with others.

Modern Soap Makers have few choices when it comes to designing and calculating soap recipes. These resources rarely have a way to store recipes with the ability to update them and make notes on the outcomes of the recipes. While there are many blogs for soapers, there should be an easy way to search, share, and save favorite recipes with other like-minded makers.

## MVP Features 

<em>Recipes:</em>
- Sign in via Google Authentication
- Add a new Recipe to see the recipe card visible on the home page with all other user-created recipes.
- Clicking the recipe card takes the User to the Recipe Details page which has weight amounts for all ingredients needed to make the recipe. This page also contains the soap description and notes about the recipe.
- A Favorite Button allows a User to add a recipe to their favorites list, whether the recipe was created by the User, or another Soaper.
- The Favorite Recipes Page allows a User to see all favorited recipes
- The Public Recipes page allows a User to see recipes by all users set to public.
<img src="https://user-images.githubusercontent.com/107942776/246680238-226e1c2e-f8be-4819-b6be-e909b2d12b99.png" width="500"/>
<img src="https://user-images.githubusercontent.com/107942776/246680233-789b08da-fcfb-4a5e-a2ed-416cd565a122.png" width="500"/>
<img src="https://user-images.githubusercontent.com/107942776/246680224-ad5f027a-e93a-4f7d-b345-b0b4f100fe51.png" width="500"/>


## Try the app yourself
[Video Walkthrough](https://www.loom.com/share/25365a2897584b56932bf286f0173da8?sid=825496a2-3a9e-481a-a53e-1a911ceb1399)

1. Clone GSD to your local machine 
```
git@github.com:ericlfrey/soap-dish-server.git
```
2. Move into the directory
```
cd soap-dish-server
```
3. Install pyenv * optional
```
pip install pyenv
```
4. Install Python [3.9.16](https://www.python.org/downloads/release/python-3916/)
5. Install pipenv
```
pip install pipenv
```
6. Start your virtual environment
```
pipenv shell
```
7. Run the Server
```
python3 manage.py runserver
```
8. Setup and run the [The Soap Dish Client](https://github.com/ericlfrey/soap-dish-client) for this project to run on local machine.



## Planning
#### ERD for The Soap Dish MVP
<img src="https://user-images.githubusercontent.com/107942776/246680192-ffd33b5b-ba25-4621-87f2-842de85e4d29.png" width="500"/>

[Link to ERD](https://dbdiagram.io/d/6477a843722eb774942b395b)


## Code Snippets

#### Recipe Model
<img src="https://user-images.githubusercontent.com/107942776/246690845-8d79f3a9-04e0-437d-8634-045917743b34.png" width="500"/>

#### RecipeView create and retrieve methods
<img src="https://user-images.githubusercontent.com/107942776/246690846-5833d480-bf9e-4ddc-a16a-63fbb9b3f773.png" width="500"/>

#### Serializers
<img src="https://user-images.githubusercontent.com/107942776/246690844-15162cbc-2a08-444d-a6f0-74a4f81d75f2.png" width="600"/>

#### Custom Actions
<img src="https://user-images.githubusercontent.com/107942776/246690847-70684fe7-6fe0-425f-80d4-8bd41a095db3.png" width="600"/>

## Tech Stacks
<div align="center">  
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>  
<a href="https://nextjs.org/" target="_blank" rel="noreferrer"> <img src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="nextjs" width="40" height="40"/>
</div>


## Contributors
- [Eric Frey](https://github.com/ericlfrey)
