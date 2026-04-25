import streamlit as st
import google.generativeai as genai

# إعدادات الهوية والواجهة
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center;'>🤖 مساعد MUNTADHER.H.ASD الذكي</h1>", unsafe_allow_html=True)

# استدعاء المفتاح من "الخزنة السرية" Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ يرجى إضافة مفتاح API في إعدادات Secrets.")
    st.stop()

# نظام ذاكرة الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("تفضل، اسألني أي شيء..."):
    # إضافة سؤال المستخدم للذاكرة والعرض
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد من الذكاء الاصطناعي
    with st.chat_message("assistant"):
        try:
            # هنا نطلب من الموديل أن يعرف نفسه دائماً بذكر اسمك
            response = model.generate_content(f"أجب كمساعد ذكي تم تطويره بواسطة المبرمج منتظر (MUNTADHER.H.ASD). السؤال هو: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"❌ حدث خطأ: {e}")

