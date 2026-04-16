import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

my_api = os.environ.get(key='MY_API_KEY')
client = genai.Client(api_key=my_api)

def call_to_api(images,option):
    prompt = f"Read this images & provide me {option} for each image separately with proper markdown"
    response = client.models.generate_content(model="gemini-3-flash-preview",contents=[images,prompt])
    return response.text
