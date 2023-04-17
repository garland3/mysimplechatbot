
import requests
import json
from config import settings

url = settings.backendurl

# url = "http://localhost:8002/run"
headers = {
    "accept": "application/json",
    "api-key": "xx1asafs9uaxlkn",
    "Content-Type": "application/json"
}
def generate_response(question):
    data = {
        "instruction": question,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # return response of the json
    return response.json()['response']





# from transformers import pipeline, set_seed

# generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
# set_seed(42)

# def generate_response(question):
#     print("Generating response for question: ", question)
#     response = generator(question, max_length=250, do_sample=True, temperature=0.7)[0]["generated_text"]
#     response = response.split(question)[1].strip()
#     return response



# import requests
# import json
# url = "http://localhost:8002/run"
# headers = { "accept": "application/json", 
#            "api-key": "xx1asafs9uaxlkn", "Content-Type": "application/json" }
# def generate_response(question):
#     data = { "instruction": question, }
#     response = requests.post(url, headers=headers, data=json.dumps(data)) # return response of the json
#     return response.json()['response']