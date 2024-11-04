import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def get_ai_description_car(model, brand, year):
    
    api_key = str(getenv('AI_API_KEY'))
    prompt = f'''Write for me a description of the car {brand} {model} {year} with a maximum of 250 characters. Write about technical information about this car model. You are a car salesman, be captivating'''
    url = "https://api.edenai.run/v2/text/chat"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_base_64": True,
        "show_original_response": False,
        "temperature": 0,
        "max_tokens": 1000,
        "tool_choice": "auto",
        "text": prompt,
        "providers": ["google"]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    response_text = dict(response_json)['google']
    generated_text = dict(response_text)['generated_text']

    return generated_text
