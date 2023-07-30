import openai
from textbase.message import Message
import json

from textbase.message import Message


class OpenAI:
    api_key = None

    @classmethod
    def generate(
        cls,
        system_prompt: str,
        message_history: list[Message],
        model="gpt-3.5-turbo",
        max_tokens=3000,
        temperature=0.7,
    ):
        assert cls.api_key is not None, "OpenAI API key is not set"
        openai.api_key = cls.api_key

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                *map(dict, message_history),
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]

    function_descriptions = [
        # Workout videos
        {
            "name": "get_workout_videos",
            "description": "Get YouTube videos for exercises in a workout routine",
            "parameters": {
                "type": "object",
                "properties": {
                    "exercises": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["exercises"]
            }
        },

        # Recipes
        {
            "name": "get_recipes",
            "description": "Get recipes based on food groups in a nutrition plan",
            "parameters": {
                "type": "object",
                "properties": {
                    "food_groups": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["food_groups"]
            }
        }
    ]

    @classmethod
    def extract_exercises(cls, latest_response):
  
      prompt = f"Extract the list of exercises from this text and return as a JSON array: {latest_response}"
      assert cls.api_key is not None, "OpenAI API key is not set"
      openai.api_key = cls.api_key
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "user", "content": prompt}],
        max_tokens=3000,
        temperature=0.7
      )
      
      exercises = json.loads(response.choices[0].message.content)
      return exercises

    @classmethod
    def extract_food_groups(cls, latest_response):

      prompt = f"Extract the food groups from this diet plan and return as a JSON array: {latest_response}"
      assert cls.api_key is not None, "OpenAI API key is not set"
      openai.api_key = cls.api_key
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        max_tokens=3000,
        temperature=0.7,
      )

      food_groups = json.loads(response.choices[0].message.content)
      return food_groups

  