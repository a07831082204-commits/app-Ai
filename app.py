import streamlit as st
import requests

# إعدادات واجهة المستخدم
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini AI")

# مفتاح الـ API (تأكد من حمايته لاحقاً)
API_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# إدخال المستخدم
if prompt := st.chat_input("كيف يمكنني مساعدتك اليوم؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # طلب الرد من الذكاء الاصطناعي
    with st.chat_message("assistant"):
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(URL, json=payload)
        
        if response.status_code == 200:
            answer = response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.error("فشل في الاتصال بالذكاء الاصطناعي.")
