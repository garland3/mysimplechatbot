from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from chatbot import generate_response
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from datetime import datetime
from database import get_single_db, UserSession, ChatMessage, get_user_session
from config import settings
from datetime import datetime, timedelta
import secrets

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

db = get_single_db() 


# Generate a secret key for signing cookies
SECRET_KEY = secrets.token_hex(32)

# Define the expiration time for session cookies
SESSION_EXPIRATION_TIME = timedelta(hours=1)

# Define the cookie name for session IDs
SESSION_COOKIE_NAME = "session_id"

# Set the cookie expiration time to the same value as the session expiration time
COOKIE_EXPIRATION_TIME = SESSION_EXPIRATION_TIME.total_seconds()


def set_session_cookie(response: JSONResponse, session_id: str):
    """
    Set the session ID cookie in the response.
    """
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=session_id,
        max_age=COOKIE_EXPIRATION_TIME,
        expires=COOKIE_EXPIRATION_TIME,
        secure=True,
        httponly=True,
    )
    

def get_session_id(request: Request):
    """
    Extract the session ID from the request cookies, if present.
    """
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    return session_id

@app.post("/chatbot")
async def chatbot(request: Request):
    print("request received at /chatbot")
    data = await request.json()
    print("data: ", data)
    question = data["question"]
    timestamp = datetime.now()
    # user_session_id = data.get('user_session_id')
    session_id= get_session_id(request)
    if session_id is not None:
        session_obj  = get_user_session(db, session_id)
    if session_id is None:
        # missing a cookie, redirect to index
        return {"response": "redirect"}
            
    db.add(ChatMessage(user_session_id=session_id, message=question, timestamp=timestamp, agent = 'user'))
    response = generate_response(question)
    # Log chat message to database
    db.add(ChatMessage(user_session_id=session_id, message=response, timestamp=timestamp, agent = 'bot'))
    db.commit()
    return {"response": response}


@app.get("/", response_class=HTMLResponse)
async def index(response: HTMLResponse):
    with open("static/index.html", "r") as f:
        html = f.read()
    # Log user session to database
    timestamp = datetime.now()
    ip = '0.0.0.0'  # replace with actual user IP
    username = 'greg'  # replace with actual authenticated user
    chat_id = 1  # replace with actual chat ID
    # when a user logs in, create a new user session    
    user_session = UserSession(ip=ip, username=username, chat_id=chat_id, start_time=timestamp)
    # add the user session to the database
    db.add(user_session)
    db.commit()
    # Then, add a cookie to the response with the user session ID
    response = HTMLResponse(content=html, status_code=200)
    response.set_cookie(key="session_id", value=str(user_session.id))
    return response

# run with 
# uvicorn main:app --reload
