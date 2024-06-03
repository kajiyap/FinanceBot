import pathlib
import textwrap
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def multiply(a:float, b:float):
    """returns a * b."""
    return a*b

model = genai.GenerativeModel('gemini-1.5-flash', tools=[multiply])
chat = model.start_chat(enable_automatic_function_calling=True)

def question(pergunta):
    response = chat.send_message(pergunta)
    return(response.text)