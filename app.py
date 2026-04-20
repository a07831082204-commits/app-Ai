import streamlit as st
import requests

# إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")

# التصميم الخارجي والعنوان
st.title("🤖 مساعد MUNTADHER.H.ASD الذكي")
st.markdown("---")

# مفتاح الـ API والروابط
API_KEY = "AIzaSyCaob5EdZ15Cry_79esFizlSkAs9VNI_yU"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# ذاكرة المحادثة (لحفظ الشات أثناء الجلسة)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("تفضل اسألني أي شيء..."):
    # عرض رسالة المستخدم وحفظها
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # طلب الرد من Gemini
    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
            # التنسيق الصحيح للبيانات المرسلة (هذا يحل خطأ 400)
            payload = {
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ]
            }
            headers = {"Content-Type": "application/json"}
            
            try:
                response = requests.post(URL, json=payload, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    # استخراج النص من استجابة جوجل
                    answer = data['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    # حفظ الرد في الذاكرة
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"خطأ من المصدر: {response.status_code}")
                    st.info("إذا استمر الخطأ، قد يحتاج مفتاح الـ API للتحديث.")
            except Exception as e:
                st.error("حدث خطأ غير متوقع أثناء الاتصال.")

# لمسة المطور في القائمة الجانبية
st.sidebar.title("MUNTADHER.H.ASD")
st.sidebar.info("تم تطوير هذا النظام الذكي بواسطة المبرمج منتظر.")
st.sidebar.write("إصدار التطبيق: 2.0")
