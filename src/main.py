from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from chatbot import generate_response
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from datetime import datetime
from database import get_single_db, UserSession, ChatMessage

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.post("/chatbot")
async def chatbot(request: Request):
    print("request received at /chatbot")
    data = await request.json()
    print("data: ", data)
    question = data["question"]
    response = generate_response(question)

    # Log chat message to database
   # Log chat message to database
    timestamp = datetime.now()
    user_session_id = data.get('user_session_id')
    with get_single_db() as db:
        db.add(ChatMessage(user_session_id=user_session_id, message=question, timestamp=timestamp))
        db.add(ChatMessage(user_session_id=user_session_id, message=response, timestamp=timestamp))
        db.commit()

    return {"response": response}


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", "r") as f:
        html = f.read()

    # Log user session to database
    timestamp = datetime.now()
    ip = '0.0.0.0'  # replace with actual user IP
    username = 'greg'  # replace with actual authenticated user
    chat_id = 1  # replace with actual chat ID
    with get_single_db() as db:
        user_session = UserSession(ip=ip, username=username, chat_id=chat_id, start_time=timestamp)
        db.add(user_session)
        db.commit()

    # Inject user session ID into HTML
    html = html.replace('{{ user_session_id }}', str(user_session.id))

    return html

# run with 
# uvicorn main:app --reload
