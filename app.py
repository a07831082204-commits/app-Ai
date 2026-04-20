import streamlit as st
import google.generativeai as genai

# إعداد الواجهة الرسمية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")

# الربط الآمن عبر Secrets (هذا هو الضمان الحقيقي)
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ لم يتم العثور على المفتاح في الخزنة السرية (Secrets).")
        st.stop()
except Exception as e:
    st.error(f"خطأ في النظام: {e}")
    st.stop()

# نظام ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة الشات
if prompt := st.chat_input("تفضل، اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception:
            st.error("❌ حدث خطأ في الاتصال بالسيرفر. يرجى التأكد من المفتاح في Secrets.")
            
