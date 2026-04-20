import streamlit as st
import requests

# --- إعدادات الواجهة باسمك الشخصي MUNTADHER.H.ASD ---
st.set_page_config(
    page_title="MUNTADHER.H.ASD AI",
    page_icon="🤖",
    layout="centered"
)

# تصميم العنوان بشكل أنيق
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# مفتاح الـ API الخاص بـ Gemini
API_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# تهيئة ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة في فقاعات شات
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة إدخال المستخدم
if prompt := st.chat_input("تفضل اسألني أي شيء، أنا بانتظارك..."):
    # إضافة رسالة المستخدم للذاكرة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # طلب الرد من الذكاء الاصطناعي
    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
            # هذا التنسيق (Payload) هو الأصح لتجنب خطأ 400
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                # إرسال الطلب باستخدام json= لضمان التنسيق الصحيح
                response = requests.post(URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    # استخراج نص الرد
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    # حفظ رد المساعد في الذاكرة
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"خطأ في الاتصال: {response.status_code}")
                    st.info("ملاحظة: تأكد من أن مفتاح الـ API صالح ولم يتم استهلاكه بالكامل.")
            except Exception as e:
                st.error(f"حدث خطأ غير متوقع: {e}")

# --- بصمة المبرمج في الشريط الجانبي ---
st.sidebar.title("MUNTADHER.H.ASD")
st.sidebar.markdown("---")
st.sidebar.write("**حالة التطبيق:** متصل ✅")
st.sidebar.info("هذا التطبيق هو مشروع برمجي خاص بمنتظر Haider.")
