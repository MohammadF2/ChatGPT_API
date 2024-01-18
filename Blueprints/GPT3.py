from flask import blueprints
import flask
import json
import openai
from Config.config import API_KEY

client = openai.OpenAI(api_key=API_KEY)


GPT_3 = blueprints.Blueprint('GPT_3', __name__)


@GPT_3.route('/query', methods=['POST'])
def query():
    data = flask.request.json
    data = "I need you to generate a story paragraph max 5 lines, using the following key words: " + data["keys"] + ", make the hero's name in the story: " + data["name"] + ", the target age for the story is make sure that the language is simple for: " + data["age"] + " years old kids, you dont need to mention the age, make the story in " + data["lang"] + "notes: " + data["notes"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": data}
        ]
    )
    return {"response": response.choices[0].message.content}

@GPT_3.route('/query_story', methods=['POST'])
def query_story():
    data = flask.request.json
    story_num = data['story_num']

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": data['query']}
        ]
    )
    return {"response": response.choices[0].message.content}