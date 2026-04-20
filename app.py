import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")

# جلب مفتاح الـ API من الخزنة السرية للموقع
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.warning("⚠️ يرجى إضافة مفتاح API في إعدادات Secrets.")
        st.stop()
except Exception as e:
    st.error(f"خطأ في إعدادات النظام: {e}")
    st.stop()

# نظام الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
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
            st.error("❌ حدث خطأ في الاتصال بالسيرفر.")
            
