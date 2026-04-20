import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")

st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# الشريط الجانبي
st.sidebar.title("إعدادات الوصول")
# المفتاح الافتراضي (تأكد من الحصول على واحد خاص بك إذا لم يعمل هذا)
default_key = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
api_key = st.sidebar.text_input("أدخل مفتاح API الخاص بك:", value=default_key, type="password")

st.sidebar.markdown("---")
st.sidebar.info("المطور: MUNTADHER.H.ASD")

# إعداد المكتبة الرسمية
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة الإدخال
if prompt := st.chat_input("اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if not api_key:
            st.error("يرجى إدخال مفتاح API في القائمة الجانبية.")
        else:
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
                
