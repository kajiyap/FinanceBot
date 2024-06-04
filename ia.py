import yfinance as yf
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def pegarValorCota(nome: str):
    suffix = ['', '.SA']
    resposta = ''
    for s in suffix:
        try:
            ticker = yf.Ticker(nome+s)
            resposta = ticker.info['currentPrice']
            if(resposta != ''):
                return resposta
        except (IndexError, KeyError) as ex:
            resposta = 'Não foi possível encontrar essa sigla.'
    
    return resposta

def pegarNomeEmpresa(nome: str):
    suffix = ['', '.SA']
    resposta = ''
    for s in suffix:
        try:
            ticker = yf.Ticker(nome+s)
            resposta = ticker.info['longName']
            if(resposta != ''):
                return resposta
        except (IndexError, KeyError) as ex:
            resposta = 'Não foi possível encontrar essa sigla.'
    
    return resposta

def pegarPais(nome: str):
    suffix = ['', '.SA']
    resposta = ''
    for s in suffix:
        try:
            ticker = yf.Ticker(nome+s)
            resposta = ticker.info['country']
            if(resposta != ''):
                return resposta
        except (IndexError, KeyError) as ex:
            resposta = 'Não foi possível encontrar essa sigla.'
    
    return resposta

def pegarUltimoDividendo(nome: str):
    suffix = ['', '.SA']
    resposta = ''
    for s in suffix:
        try:
            ticker = yf.Ticker(nome+s)
            resposta = ticker.dividends.array[-1]
            resposta = resposta
            if(resposta != ''):
                return resposta
        except (IndexError, KeyError) as ex:
            resposta = 'Não foi possível encontrar essa sigla.'
    
    return resposta

model = genai.GenerativeModel('gemini-1.5-flash', tools=[pegarValorCota, pegarNomeEmpresa, pegarUltimoDividendo, pegarPais])
chat = model.start_chat(enable_automatic_function_calling=True)

def question(pergunta):
    response = chat.send_message(pergunta)
    return(response.text)