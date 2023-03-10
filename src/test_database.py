# %%
# Test the database
# 
from  datetime import datetime
import random
from database import get_db, UserSession, ChatMessage


def test_make_user_session():
    timestamp = datetime.now()
    ip = '127.0.0.1'
    username = 'bob'
    chat_id = 1
    db =next( get_db())
    user_session = UserSession(ip=ip, username=username, chat_id=chat_id, start_time=timestamp)
    db.add(user_session)
    db.commit()
    assert user_session.id is not None
    print("user_session.id: ", user_session.id)
    print("All OK")
    
def test_make_chat_message():
    timestamp = datetime.now()
    user_session_id = 1
    message = 'hello'
    db = next(get_db())
    
    # make a user session 1st
    ip = '127.0.0.1'
    username = f'bob_{random.randint(1, 100)}'
    chat_id = random.randint(1, 100)
    starttime = datetime.now()
    user_session = UserSession(ip=ip, username=username, chat_id=chat_id, start_time=starttime)
    db.add(user_session)
    db.commit()
    print("user_session.id: ", user_session.id)
    session_id = user_session.id
    
    chat_message = ChatMessage(user_session_id=session_id, message=message,
                               timestamp=timestamp)
    db.add(chat_message)
    db.commit()
    assert chat_message.id is not None
    print("chat_message.id: ", chat_message.id)
    print("All OK for chat_message")
      

# make a function test if ipython is 
# running in interactive mode or not
def in_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
    
if in_ipython():
    # test_make_user_session()
    test_make_chat_message()

# %%
# # test1
# def test1():
#     user_session = db.query(UserSession).first()
#     print(user_session)
#     print(user_session.chat_messages)
#     print(user_session.chat_messages[0].message)