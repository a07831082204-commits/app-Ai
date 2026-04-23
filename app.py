import streamlit as st
import google.generativeai as genai

# إعدادات الهوية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🤖 مساعد MUNTADHER.H.ASD الذكي</h1>", unsafe_allow_status=True)

# استدعاء المفتاح من الخزنة السرية (حماية 100%)
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ خطأ في الإعدادات السرية. يرجى مراجعة مبرمج النظام.")
    st.stop()

# نظام الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تفضل، اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("❌ فشل الاتصال بالسيرفر. المفتاح قد يكون منتهي الصلاحية.")
            
