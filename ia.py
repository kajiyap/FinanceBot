import datetime
import pandas as pd
import pandas_datareader
import yfinance as yf
import google.generativeai as genai
import os
import setuptools
from dotenv import load_dotenv, dotenv_values

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def pegarCotas (nome: str, period: int=1):
    ticker = yf.Ticker(nome)
    try:
        return ticker.history(period=f"{period}d")['Close'][0]
    except IndexError as ex:
        return 'Não foi possível encontrar essa sigla.'

def multiply(a:float, b:float):
    """returns a * b."""
    return a*b

model = genai.GenerativeModel('gemini-1.5-flash', tools=[multiply, pegarCotas])
chat = model.start_chat(enable_automatic_function_calling=True)

def question(pergunta):
    response = chat.send_message(pergunta)
    return(response.text)