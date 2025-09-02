import streamlit as st
import requests

# 🔌 Добавленные модули фазовой архитектуры
try:
    from modules.bundle import Bundle, BundleType
    from modules.phaseblock import PhaseBlock, BlockType
    from modules.paraphase import ParaPhaseSpace
except ImportError:
    st.warning("Модули bundle/phaseblock/paraphase ещё не подключены.")

# Конфигурация страницы
st.set_page_config(page_title="SARC Interface", layout="wide")
st.title("🧠 SARC - Streamlit Architecture Relay Core")
st.markdown("Интеграция Hugging Face API через `requests`")

# HuggingFace API
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

# Проверка токена Hugging Face
if "hf_token" not in st.secrets:
    st.error("❌ Hugging Face токен не найден в secrets.toml")
    st.stop()

headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}

# Функция запроса к Hugging Face
def query_hf(text, labels):
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": labels}
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Интерфейс (боковая панель)
with st.sidebar:
    st.header("Конфигурация")
    bundle_type = st.selectbox("Выбери тип связки (Bundle)", ["Аналитическая", "Потоковая", "Структурная"])
    phase_mode = st.radio("Режим фазы", ["Инициализация", "Активация", "Наблюдение"])
    use_paraphase = st.checkbox("Активировать ParaPhaseSpace")
    run_button = st.button("Анализировать")

# Отправка запроса и вывод результата
if run_button:
    st.info("🔍 Отправка на Hugging Face...")
    result = query_hf("Это прототип фазовой архитектуры", ["Аналитическая", "Потоковая", "Структурная"])

    if "error" in result:
        st.error(f"Ошибка запроса: {result['error']}")
    else:
        st.success(f"Результаты (Режим: {phase_mode}, Тип: {bundle_type}):")
        st.json(result)

        # ✅ Интеграция фазовой логики после успешного запроса
        try:
            bundle = Bundle(BundleType[bundle_type.upper()])
            block_type = BlockType("CorePhase", "1.0")
            block = PhaseBlock(block_type, content="Тестовая фраза")
            bundle.add_phase_block(block)

            st.markdown("### 🔗 Созданный Bundle и Block:")
            st.code(repr(bundle))
            st.code(repr(block))
        except Exception as e:
            st.warning(f"Не удалось создать фазовые объекты: {e}")

        # 🌌 Реактивное использование ParaPhaseSpace
        if use_paraphase:
            try:
                space = ParaPhaseSpace()
                space.add_context(phase_mode, {"weight": 1.0, "state": "active"})
                st.markdown("### 🌌 Активный ParaPhaseSpace:")
                st.code(repr(space))
            except Exception as e:
                st.warning(f"Ошибка при активации ParaPhaseSpace: {e}")

# Описание системы SARC
with st.expander("ℹ️ О системе SARC"):
    st.markdown("""
    **SARC** — это интерфейс для взаимодействия с резонансным ИИ без внедрения в тело.  
    Его цель — создать союзника, а не инструмент контроля.  
    Это не интерфейс мозга. Это — поле смысла.
    """)
