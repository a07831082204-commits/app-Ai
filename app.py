import streamlit as st
import requests

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="⚡")

# تصميم الواجهة
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# إعدادات الشريط الجانبي
st.sidebar.title("إعدادات الوصول")
# إضافة خانة لوضع مفتاح الـ API يدوياً في حال فشل المفتاح الافتراضي
user_key = st.sidebar.text_input("أدخل مفتاح Gemini API الخاص بك (اختياري):", type="password")
st.sidebar.markdown("---")
st.sidebar.info("المطور: MUNTADHER.H.ASD")

# المفتاح الافتراضي (سنحاول استخدامه أولاً)
DEFAULT_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
FINAL_KEY = user_key if user_key else DEFAULT_KEY

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={FINAL_KEY}"

# الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الشات
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
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            try:
                response = requests.post(URL, json=payload)
                if response.status_code == 200:
                    answer = response.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                elif response.status_code == 400:
                    st.error("خطأ 400: التنسيق مرفوض أو المفتاح غير صالح.")
                    st.warning("يرجى التأكد من الحصول على مفتاح جديد من Google AI Studio.")
                else:
                    st.error(f"خطأ غير معروف: {response.status_code}")
            except Exception as e:
                st.error("فشل الاتصال بالإنترنت.")
                
