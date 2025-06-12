import streamlit as st
import time
from utils import *

st.set_page_config(page_title="CupidoGPT 💘", page_icon="💌")
st.title("💘 Bem-vinda ao CupidoGPT")



if "stage" not in st.session_state:
    st.session_state.list_for_vini = {}
    write_slow("Olá, sou um cupido digital treinado com as memórias mais lindas do seu relacionamento!")
    st.image("./images/1.jpg", use_container_width=True)
    write_slow("O vini me falou demais sobre vc, então eu vou fz um quiz sobre o que ele me contou... Espero que goste...")
    st.session_state.stage = 0

# -----------------------------
# Bora começar?
# -----------------------------
if st.session_state.stage == 0:
    st.subheader("Vamos começar👀😻?")
    if st.button("Siiiiiiiiiiiiiiiiiiim"):
        st.session_state.stage = 1
    
# -----------------------------
# Pergunta 1
# -----------------------------
elif st.session_state.stage == 1:
    st.subheader("📍 Pergunta 1: O que o vini mais ama de você?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Seu Corpo"):
            st.session_state.resposta1 = "Seu Corpo"
            st.image("./images/3.jpg", use_container_width=True)
            st.write("Ele adora seu corpo, mas não é só isso que ele ama em você!")
    with col2:
        if st.button("Seu Coração"):
            st.session_state.resposta1 = "Seu Coração"
            st.image("./images/2.jpg", use_container_width=True)
            st.write("Ele adora seu Coração, mas não é só isso que ele ama em você!")
    with col3:
        if st.button("Seu jeitinho"):
            st.session_state.resposta1 = "Seu jeitinho"
            st.image("./images/4.jpg", use_container_width=True)
            st.write("Ele adora seu jeitinho, mas não é só isso que ele ama em você!")

    if "resposta1" in st.session_state:
        st.session_state.list_for_vini['Perguta 1'] = st.session_state.resposta1
        st.write("Ele não cansa de falar o quanto ele ama você inteirinha!💋")
        if st.button("Próxima pergunta ➡️"):
            st.session_state.stage = 2

# -----------------------------
# Pergunta 2
# -----------------------------
elif st.session_state.stage == 2:
    st.subheader("📍 Pergunta 2: Qual dessas imagens mais representa Como você queria estar agora?")

    col1, col2, col3 = st.columns(3)
    st.session_state.resposta2 = False

    # Inicializa estados de clique
    for i in ["img1", "img2", "img3"]:
        if i not in st.session_state:
            st.session_state[i] = False

    with col1:
        if st.button("Sofazinho com ele"):
            st.session_state.img1 = True
        st.image("./images/5.jpg", use_container_width=True)
        if st.session_state.img1:
            st.session_state.list_for_vini['Perguta 2'] = "Sofazinho com ele"
            st.session_state.resposta2 = True

    with col2:
        if st.button("Dormindo juntinhos"):
            st.session_state.img2 = True
        st.image("./images/6.jpg", use_container_width=True)
        if st.session_state.img2:
            st.session_state.list_for_vini['Perguta 2'] = "Dormindo juntinhos"
            st.session_state.resposta2 = True

    with col3:
        if st.button("Se divertindo com ele"):
            st.session_state.img3 = True
        st.image("./images/7.jpg", use_container_width=True)
        if st.session_state.img3:
            st.session_state.list_for_vini['Perguta 2'] = "Se divertindo com ele"
            st.session_state.resposta2 = True

    if st.session_state.resposta2:
        st.write("Ele adora quando você está assim, juntinho dele! não importa o que vcs fazem juntos 🥰")
        if st.button("Bora pra próxima?"):
            st.session_state.stage = 3
        
# -----------------------------
# pausa para apreciar a beleza
# -----------------------------
elif st.session_state.stage == 3:
    st.subheader("pausa para apreciar sua beleza 😍")
    write_slow('"pelamordedeus olha essa mulher perfeita linda maravilhosa encantadora"')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./images/11.jpg", use_container_width=True)
        st.image("./images/12.jpg", use_container_width=True)
        st.image("./images/13.jpg", use_container_width=True)
    with col2:
        st.image("./images/14.jpg", use_container_width=True)
        st.image("./images/15.jpg", use_container_width=True)
        st.image("./images/16.jpg", use_container_width=True)
    with col3:
        st.image("./images/17.jpg", use_container_width=True)
        st.image("./images/18.jpg", use_container_width=True)
        st.image("./images/19.jpg", use_container_width=True)
    write_slow("Agora vamos para a próxima pergunta, espero que esteja gostando do quiz até agora!")
    if st.button("Bora pra próxima?"):
        st.session_state.stage = 4

# -----------------------------
# Pergunta 3
# -----------------------------
elif st.session_state.stage == 4:
    st.subheader("📍 Pergunta 3: O quanto o vini te ama?")
    x = st.slider('O quanto o vini te ama numa escala de 0 a 10?', min_value=0, max_value=11)
    
    if x == 11:
        st.write("Isso mesmo, 11, ele te ama mais que tudo nesse mundo❤️‍🔥")
        if st.button("Bora pra próxima?"):
            st.session_state.stage = 5
    elif x == 10:
        st.write("Bem... ele te ama muito, mas n SÓ 10...")
    else:
        st.write(f"Ah não, {x} não é uma opção! Ele te ama muito mais que isso! 😢")

elif st.session_state.stage == 5:
    st.subheader("📍 Pergunta 4: Se você, hipotéticamente falando, escolhesse ir para uma cafeteria, qual vc iria??")
    flag = False
    resposta = st.text_input("Qual cafeteria você escolheria?")

    if resposta.lower() == 'monkafé' or resposta.lower() == 'monkafe' or resposta.lower() == 'monkafezinho' or resposta.lower() == 'moncafe' or resposta.lower() == 'moncafé' or resposta.lower() == 'moncafézinho':
        flag = True
        st.write("Ah, o Monkafé é perfeito! Ele adora lá! ☕️❤️")

    if resposta != '' and flag == False:
        st.write(f'Nooooooossa, o vini advinhou mesmo, kkk... claro, ele é fera, ele sabia que vc iria escolher {resposta}')
    
    if st.button("Bora pra próxima?") and resposta != "":
        st.session_state.list_for_vini['Perguta 3'] = resposta
        st.session_state.stage = 6

# -----------------------------
# Pergunta 4
# -----------------------------
elif st.session_state.stage == 6:
    st.subheader("📍 Pergunta 4: Com qual personagem o vini mais acha q vc se parece??")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Himezinha"):
            st.session_state.resposta3 = "Himezinha"
            st.image("./images/8.jpg", use_container_width=True)
            st.write("Super irritadora e se faz de série mas é uma manteguinha")
    with col2:
        if st.button("Peroninha"):
            st.session_state.resposta3 = "Peroninha"
            st.image("./images/9.jpg", use_container_width=True)
            st.write("Uma gordinha igualzinha vc")
    with col3:
        if st.button("bixinho"):
            st.session_state.resposta3 = "Bixinho"
            st.image("./images/10.jpg", use_container_width=True)
            st.write("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    if "resposta3" in st.session_state:
        st.session_state.list_for_vini['Perguta 4'] = st.session_state.resposta3
        st.write("Todas fofuchas iguaizinhas e lindas, assim como você! 💖")
        if st.button("Próxima pergunta ➡️"):
            st.session_state.stage = 7


elif st.session_state.stage == 7:
    st.subheader("Quando o vini me mostrou esse vídeo, eu não consegui parar de rir, vamos apreciar juntos? 🍿")
    time.sleep(1)
    st.video("images/1.mp4")
    if st.button("Próxima pergunta ➡️"):
            st.session_state.stage = 8

elif st.session_state.stage == 8:
    st.subheader("📍 Pergunta 5: Ultima pergunta")
    st.write('Se você pudesse escolher uma nota pro presente do vini, qual seria?')
    resposta = st.text_input("mimde uma nota")
    if resposta.lower() == '10':
        st.write('awwwwn obrigado, fico muito feliz já q ele me fez ontem de noite kskskskskskskskskskskskss')
    elif resposta.lower() == '0':
        st.write("n me ama nem um pouco")
    else:
        st.write('obrigado pela nota, vou tentar melhorar mais ainda e vou passar pra ele')
    if st.button("Confirmar a resposta"):
        st.session_state.list_for_vini['Perguta 5'] = resposta
        st.session_state.stage = 9
# -----------------------------
# ETAPA FINAL
# -----------------------------
elif st.session_state.stage == 9:
    st.balloons()
    write_slow("💌 Processando com muito amor...")
    time.sleep(2)
    st.image("./images/20.jpg", use_container_width=True)
    send_telegram_message(dict_to_txt(st.session_state.list_for_vini))
    st.subheader("🌟 Fim do quiz! Espero que tenha gostado, o vini se esforçou muito para me por no Ar 💌")
    st.write()
    st.write("Ele me contou que vocês têm uma história linda e cheia de momentos especiais.")
    st.write("Você é a razão do sorriso dele, uma princesa, o castelo de vc vai ser bem lindo!! 👑")
    st.write("Até a próxima babs babs, espero que tenha gostado!")
