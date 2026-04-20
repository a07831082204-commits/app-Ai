import streamlit as st
import requests
import json

# --- إعدادات الواجهة باسم MUNTADHER.H.ASD ---
st.set_page_config(
    page_title="MUNTADHER.H.ASD AI",
    page_icon="⚡",
    layout="centered"
)

st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# مفتاح الـ API والرابط المحدث (v1 بدلاً من v1beta لحل مشكلة 404)
API_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة الإدخال
if prompt := st.chat_input("تفضل، أنا اسمعك..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("جاري الاتصال بالعقل الاصطناعي..."):
            # التنسيق الجديد للبيانات
            headers = {'Content-Type': 'application/json'}
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(URL, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"حدث خطأ في الخادم (رمز: {response.status_code})")
                    st.info("نصيحة: إذا استمر الخطأ، جرب إنشاء مفتاح جديد من Google AI Studio.")
            except Exception as e:
                st.error("فشل الاتصال بالإنترنت.")

# القائمة الجانبية
st.sidebar.title("MUNTADHER.H.ASD")
st.sidebar.markdown("---")
st.sidebar.success("تم التطوير بواسطة: MUNTADHER.H.ASD")
st.sidebar.write("إصدار الموديل: Gemini Pro")
