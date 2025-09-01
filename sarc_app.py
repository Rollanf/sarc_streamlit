import streamlit as st

st.set_page_config(page_title="SARC Interface", layout="wide")

st.title("🧠 SARC - Streamlit Architecture Relay Core")
st.markdown("Прототип интерфейса. Архитектура работает через HuggingFace и Codesphere.")

# Тестовые элементы интерфейса
with st.sidebar:
    st.header("Конфигурация")
    bundle_type = st.selectbox("Выбери тип связки (Bundle)", ["Аналитическая", "Потоковая", "Структурная"])
    phase_mode = st.radio("Режим фазы", ["Инициализация", "Активация", "Наблюдение"])

if bundle_type and phase_mode:
    st.success(f"Активирована связка: **{bundle_type}** в режиме **{phase_mode}**")

st.markdown("Здесь можно будет добавлять: блоки, связки, фазовые линии и другие элементы.")
