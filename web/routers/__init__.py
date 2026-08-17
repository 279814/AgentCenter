import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from AuthRouter import auth_router
from SessionRouter import session_router
from ChatRouter import chat_router