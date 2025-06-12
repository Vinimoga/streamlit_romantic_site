import streamlit as st
import random

st.set_page_config(page_title="CupidoGPT 💘", page_icon="💌")

# --- Cabeçalho ---
st.title("💘 Bem-vinda ao CupidoGPT")
st.write("Olá, sou um cupido digital treinado com as memórias mais lindas do seu relacionamento!")
st.write("Vamos começar com uma pergunta...")

# --- Pergunta romântica ---
pergunta = "Qual foi o lugar do primeiro encontro de vocês?"
resposta = st.text_input(pergunta)

# --- Resposta e mensagem personalizada ---
if resposta:
    st.write("💌 Processando com muito amor...")

    # Simulação de uma mensagem romântica com IA
    mensagens = [
        f"Ai... só de lembrar do nosso primeiro encontro em {resposta}, meu coração dispara! 💓",
        f"Ah, {resposta}... foi lá que tudo começou. O tempo parou e nossos olhares se encontraram. ✨",
        f"Nunca vou esquecer aquele dia em {resposta}. Foi quando meu mundo ganhou cor. 🌈"
    ]
    mensagem_escolhida = random.choice(mensagens)
    st.success(mensagem_escolhida)

    # Mensagem extra
    st.markdown("### 💝 Surpresa!")
    st.write("Você é parte da história de amor mais linda que esse cupido já conheceu.")
    st.write("Prepare-se: o seu príncipe preparou algo especial pra hoje...")

