import yfinance as yf
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def pegarCotas (nome: str, period: int=1):
    suffix = ['', '.SA']
    resposta = ''
    for s in suffix:
        try:
            ticker = yf.Ticker(nome+s)
            resposta = ticker.history(period=f"{period}d")['Close'][0]
        except IndexError as ex:
            resposta = 'Não foi possível encontrar essa sigla.'
    
    return resposta

def multiply(a:float, b:float):
    """returns a * b."""
    return a*b

model = genai.GenerativeModel('gemini-1.5-flash', tools=[multiply, pegarCotas])
chat = model.start_chat(enable_automatic_function_calling=True)

def question(pergunta):
    response = chat.send_message(pergunta)
    return(response.text)