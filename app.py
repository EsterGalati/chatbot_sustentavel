import streamlit as st
import json
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def carregar_base_local():
    try:
        with open("perguntas_respostas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Arquivo 'perguntas_respostas.json' não encontrado!")
        return {}
    except json.JSONDecodeError:
        st.error("Erro ao ler o arquivo 'perguntas_respostas.json'. Verifique se o formato está correto!")
        return {}

base_local = carregar_base_local()

def normalizar_pergunta(pergunta):
    return pergunta.lower().strip("?").strip()

def resposta_local(pergunta):
    pergunta_normalizada = normalizar_pergunta(pergunta)
    for chave, resposta in base_local.items():
        if normalizar_pergunta(chave) == pergunta_normalizada:
            return resposta
    return None

def resposta_gpt(pergunta):
    prompt = f"Você é um assistente educativo e ambiental. Responda de forma clara e amigável: {pergunta}"
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um especialista em sustentabilidade e educação ambiental."},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao consultar a IA: {e}"

st.set_page_config(page_title="EcoBot ♻️", page_icon="🌱")
st.title("🌱 EcoBot - Chatbot de Sustentabilidade")

st.write("Digite sua pergunta sobre meio ambiente, consumo consciente ou sustentabilidade:")

pergunta = st.text_input("Sua pergunta", "")

if st.button("Perguntar"):
    if pergunta.strip() == "":
        st.warning("Por favor, digite uma pergunta.")
    else:
        resposta = resposta_local(pergunta)
        if resposta:
            st.success("✅ Resposta:")
            st.write(resposta)
        else:
            st.info("✅ Resposta da IA (GPT-4):")
            resposta = resposta_gpt(pergunta)
            st.write(resposta)
