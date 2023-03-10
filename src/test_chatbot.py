# %%
from chatbot import generate_response
# %%

def test_generate_response():
    question = "What is your name?"
    response = generate_response(question)
    assert isinstance(response, str)
    return response
# %%
test_generate_response()
# %%
