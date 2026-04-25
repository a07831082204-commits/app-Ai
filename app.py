import streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة والهوية
st.set_page_config(page_title="MUNTADHER.H.ASD AI", page_icon="🤖", layout="centered")

# 2. كود سحري لإخفاء العلامة المائية وشعار Streamlit تماماً
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .viewerBadge_container__1QS1n {display: none !important;}
            div.stDeployButton {display: none !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. تصميم واجهة رأس الصفحة
st.markdown("<h1 style='text-align: center; color: #00FFA2;'>🤖 مساعد MUNTADHER.H.ASD الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>نسخة احترافية مستقرة - بدون علامات مائية</p>", unsafe_allow_html=True)
st.divider()

# 4. الربط مع الذكاء الاصطناعي (Gemini) عبر الخزنة السرية
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ يرجى إضافة GEMINI_API_KEY في إعدادات Secrets لتفعيل العقل الذكي.")
    st.stop()

# 5. نظام ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة بتنسيق أنيق
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. استقبال ومعالجة أسئلة المستخدم
if prompt := st.chat_input("تفضل، اسألني أي شيء..."):
    # إضافة سؤال المستخدم للذاكرة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد من الذكاء الاصطناعي
    with st.chat_message("assistant"):
        try:
            # توجيه الموديل ليعرف من هو المطور
            full_prompt = f"أنت مساعد ذكي متطور، مبرمجك ومطورك هو منتظر (MUNTADHER.H.ASD). أجب على هذا السؤال بذكاء: {prompt}"
            response = model.generate_content(full_prompt)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("❌ حدث خطأ في الاتصال بالسيرفر، تأكد من صلاحية مفتاح API.")
            
