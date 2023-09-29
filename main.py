import json
import os
from dotenv import load_dotenv

# from langchain import HuggingFaceHub, LLMChain
import requests

# from pydantic import model_validator


load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}


# @model_validator(pre=False, skip_on_failure=True)
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query("Can you please let us know more details about your ")
