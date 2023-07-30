# api.py

import os
import requests

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY') 

def get_workout_videos(exercises):

  videos = []

  for exercise in exercises:

    response = requests.get(
      "https://youtube.googleapis.com/youtube/v3/search",
      params={
        "key": YOUTUBE_API_KEY,
        "q": f"{exercise} workout video",
        "type": "video",
        "part": "snippet"
      }  
    )

    # Extract video data from response
    data = response.json()
    video = {
      "title": data["items"][0]["snippet"]["title"],  
      "id": data["items"][0]["id"]["videoId"],
      "thumbnail": data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    }

    videos.append(video)

  return videos


EDAMAM_APP_ID = os.getenv('EDAMAM_APP_ID')
EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')

def get_recipes(food_groups):

  recipes = []

  for group in food_groups:
  
    response = requests.get(
      "https://api.edamam.com/api/recipes/v2",
      params = {
        "type": group,
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_API_KEY
      }
    )

    # Extract recipe data from response
    recipe = {
      "label": response["hits"][0]["recipe"]["label"],
      "url": response["hits"][0]["recipe"]["url"],
      "image": response["hits"][0]["recipe"]["image"]  
    }

    recipes.append(recipe)

  return recipes