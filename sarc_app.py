import streamlit as st
import requests

st.set_page_config(page_title="SARC Interface", layout="wide")
st.title("🧠 SARC - Streamlit Architecture Relay Core")
st.markdown("Интеграция Hugging Face API через `requests`")

# HuggingFace API
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}

def query_hf(text, labels):
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": labels}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Интерфейс
with st.sidebar:
    st.header("Конфигурация")
    bundle_type = st.selectbox("Выбери тип связки (Bundle)", ["Аналитическая", "Потоковая", "Структурная"])
    phase_mode = st.radio("Режим фазы", ["Инициализация", "Активация", "Наблюдение"])
    run_button = st.button("Анализировать")

if run_button:
    st.write("🔍 Отправка на Hugging Face...")
    result = query_hf("Это прототип фазовой архитектуры", ["Аналитическая", "Потоковая", "Структурная"])
    st.success("Результаты:")
    st.json(result)