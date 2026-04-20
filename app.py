import streamlit as st
import requests
import json

# --- إعدادات الواجهة باسمك الشخصي ---
st.set_page_config(
    page_title="MUNTADHER.H.ASD AI",
    page_icon="🤖",
    layout="centered"
)

# تصميم العنوان
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# --- إعدادات الربط مع Gemini ---
# ملاحظة: هذا المفتاح يعمل الآن، لاحقاً يمكنك استبداله بمفتاحك الخاص
API_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# تهيئة ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة إدخال المستخدم
if prompt := st.chat_input("تفضل اسألني أي شيء، أنا بانتظارك..."):
    # إضافة رسالة المستخدم للذاكرة والعرض
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # طلب الرد من الذكاء الاصطناعي
    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(URL, headers=headers, data=json.dumps(data))
                if response.status_code == 200:
                    result = response.json()
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    # حفظ رد المساعد في الذاكرة
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"خطأ في الاتصال: {response.status_code}")
            except Exception as e:
                st.error(f"حدث خطأ غير متوقع: {e}")

# --- بصمة المبرمج في الشريط الجانبي ---
st.sidebar.title("معلومات التطبيق")
st.sidebar.markdown("---")
st.sidebar.write("**المبرمج والمطور:**")
st.sidebar.success("MUNTADHER.H.ASD")
st.sidebar.write("يعمل هذا التطبيق بواسطة تقنيات Gemini العالمية.")

