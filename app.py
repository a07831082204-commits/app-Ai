import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")

# جلب المفتاح من الخزنة السرية للموقع
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("المفتاح السري غير مضاف في إعدادات الموقع.")
    st.stop()

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("حدث خطأ في الاتصال.")
            
