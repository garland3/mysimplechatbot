from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
set_seed(42)

def generate_response(question):
    response = generator(question, max_length=250, do_sample=True, temperature=0.7)[0]["generated_text"]
    return response
