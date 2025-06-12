import time
import streamlit as st
import random
import argparse
import requests

def write_slow(mensagem):
    placeholder = st.empty()
    texto = ""
    for letra in mensagem:
        texto += letra
        placeholder.markdown(f"##### {texto}")
        time.sleep(0.01)
    time.sleep(1)

def send_telegram_message(message):
    token = "7824531499:AAFf1W5LuI112-oIz2T_L4UyPSvQ8iGEfSc"  
    chat_id = "7823372332"   
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Erro ao enviar mensagem: {response.text}")
    return response

def main():
    parser = argparse.ArgumentParser(description="Enviar mensagem para o Telegram via bot.")
    parser.add_argument("--message", required=True, help="Mensagem a ser enviada")
    args = parser.parse_args()

    response = send_telegram_message(args.message)
    print("Resposta da API:", response.text)

if __name__ == "__main__":
    main()

def dict_to_txt(dict):
    mensagem = "{"
    for key, value in dict.items():
        mensagem += f"'{key}': '{value}', "
    mensagem += "}"
    return mensagem