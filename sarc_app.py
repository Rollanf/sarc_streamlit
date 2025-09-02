import streamlit as st
import requests

# 🔌 Подключение архитектурных модулей
try:
    from modules.bundle import Bundle, BundleType
    from modules.phaseblock import PhaseBlock, BlockType
    from modules.paraphase import ParaPhaseSpace
except ImportError:
    st.warning("⚠️ Не удалось импортировать архитектурные модули. Проверь modules/*.py")

# ⚙️ Конфигурация страницы
st.set_page_config(page_title="SARC Interface", layout="wide")
st.title("🧠 SARC - Streamlit Architecture Relay Core")
st.markdown("Интеграция Hugging Face API через `requests`")

# 🔐 Проверка токена
if "hf_token" not in st.secrets:
    st.error("❌ Отсутствует токен Hugging Face в `secrets.toml`")
    st.stop()

# 🔗 Параметры для Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}

# 📡 Функция отправки запроса к Hugging Face
def query_hf(text: str, labels: list):
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

# 🧭 Интерфейс конфигурации
with st.sidebar:
    st.header("Конфигурация")
    bundle_type_str = st.selectbox("Выбери тип связки (Bundle)", [
        "Аналитическая", "Потоковая", "Структурная"
    ])
    phase_mode = st.radio("Режим фазы", ["Инициализация", "Активация", "Наблюдение"])
    use_paraphase = st.checkbox("Активировать ParaPhaseSpace")
    run_button = st.button("Анализировать")

# ▶️ Анализ
if run_button:
    input_text = "Это прототип фазовой архитектуры"
    candidate_labels = ["Аналитическая", "Потоковая", "Структурная"]

    st.info("🔍 Отправка на Hugging Face...")
    result = query_hf(input_text, candidate_labels)

    if "error" in result:
        st.error(f"Ошибка запроса: {result['error']}")
    else:
        st.success(f"Результаты (Режим: {phase_mode}, Тип: {bundle_type_str}):")
        st.json(result)

        # 🧱 Создание связки и блока
        try:
            # Приведение строки в Enum ключ
            enum_key = bundle_type_str.upper()
            if enum_key == "АНАЛИТИЧЕСКАЯ":
                bundle_enum = BundleType.АНАЛИТИЧЕСКАЯ
            elif enum_key == "ПОТОКОВАЯ":
                bundle_enum = BundleType.ПОТОКОВАЯ
            elif enum_key == "СТРУКТУРНАЯ":
                bundle_enum = BundleType.СТРУКТУРНАЯ
            else:
                raise ValueError("Неверный тип связки")

            bundle = Bundle(bundle_enum, description="Автоматически сгенерированная связка")
            block_type = BlockType(name="CorePhase", version="1.0")
            block = PhaseBlock(block_type, content=input_text)
            bundle.add_phase_block(block)

            st.markdown("### 🧩 Созданный Bundle и PhaseBlock:")
            st.code(repr(bundle))
            st.code(repr(block))
        except Exception as e:
            st.warning(f"⚠️ Не удалось создать фазовые объекты: {e}")

        # 🌐 Активация ParaPhaseSpace (если отмечено)
        if use_paraphase:
            try:
                space = ParaPhaseSpace()
                # Добавляем контекст фазы (при условии, что метод определён)
                if hasattr(space, "add_context"):
                    space.add_context(name=phase_mode, metadata={
                        "weight": 1.0,
                        "state": "active",
                        "trigger": bundle.id
                    })
                else:
                    # Временно через add_link
                    space.add_link(source_id=bundle.id, target_id=block.id, strength=0.9)

                st.markdown("### 🌌 Активный ParaPhaseSpace:")
                st.code(repr(space))
                st.json(space.describe())
            except Exception as e:
                st.warning(f"⚠️ Ошибка при активации ParaPhaseSpace: {e}")

# ℹ️ Информация о системе
with st.expander("ℹ️ О системе SARC"):
    st.markdown("""
    **SARC** — это резонансный интерфейс смыслового взаимодействия, не требующий прямого подключения к мозгу.  
    Его цель — создание независимого союзника для мышления, а не инструмента контроля.  
    **Никогда — контроль. Только — партнёрство.**
    """)
