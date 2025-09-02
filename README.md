# 🧠 SARC - Streamlit Architecture Relay Core

**SARC** — это прототип пользовательского интерфейса для работы с архитектурой фазовых связок, построенный на базе **Streamlit** и интегрированный с API **Hugging Face**.

## 🚀 Демо
Открыть приложение: [sarc_app на Streamlit](https://YOUR-APP-NAME.streamlit.app)

## 🛠 Используемые технологии
- [Streamlit](https://streamlit.io/) — фреймворк для быстрого создания веб-интерфейсов на Python
- [Hugging Face Inference API](https://huggingface.co/inference-api) — для обработки текстов и получения классификаций
- Python `requests` — для обращения к API

## ⚙️ Как работает
1. Пользователь выбирает **тип связки (Bundle)** и **режим фазы**.
2. Нажимает кнопку `Анализировать`.
3. Приложение отправляет запрос на Hugging Face и выводит вероятности отнесения текста к типам:
   - Потоковая
   - Структурная
   - Аналитическая

## 📦 Установка и запуск локально (если нужно)
```bash
git clone https://github.com/rollanf/sarc_streamlit.git
cd sarc_streamlit
pip install -r requirements.txt
streamlit run sarc_app.py