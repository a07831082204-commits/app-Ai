import streamlit as st

# الهوية
st.set_page_config(page_title="MUNTADHER.H.ASD AI")

# تصحيح الخطأ الذي ظهر في صورتك
st.markdown("<h1 style='text-align: center;'>🤖 مساعد MUNTADHER.H.ASD الذكي</h1>", unsafe_allow_html=True)

st.write("أهلاً بك في تطبيقي الخاص!")

# نظام بسيط للدردشة للتجربة
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("اكتب رسالتك هنا...")
if user_input:
    st.session_state.chat_history.append(("أنت", user_input))
    st.session_state.chat_history.append(("المساعد", "أنا أعمل الآن بنجاح!"))

for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")
    
