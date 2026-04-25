import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة والهوية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🤖 مساعد MUNTADHER.H.ASD الذكي</h1>", unsafe_allow_html=True)

# استدعاء المفتاح من Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # قمنا بتغيير اسم النموذج هنا لضمان العمل (gemini-pro)
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ يرجى إضافة مفتاح API في إعدادات Secrets.")
    st.stop()

# نظام الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال الأسئلة
if prompt := st.chat_input("تفضل، اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # طلب الرد
            response = model.generate_content(f"أنت مساعد ذكي طوره المبرمج منتظر (MUNTADHER.H.ASD). السؤال هو: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"حدث خطأ في الاتصال: {str(e)}")
            
