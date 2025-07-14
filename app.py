# Theme & CSS
import streamlit as st
st.markdown(open(".streamlit/config.toml").read(), unsafe_allow_html=True)
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #E8EAF6, #FFF); }
[data-testid="stSidebar"] { background-color: #F0F2F6; }
h2 { color: #1E1E2F !important; }
.stButton>button { background-color: #1E1E2F; color: #FFF; border-radius:8px; }
</style>
""", unsafe_allow_html=True)

# Stylable Card
from streamlit_extras.stylable_container import stylable_container
with stylable_container(key="card1", css_styles="""
    {border-radius:15px;box-shadow:0 4px 12px rgba(0,0,0,0.1);padding:20px;background:#fff;}
"""):
    st.metric("🏆 Total Revenue", "$500K", delta="+15%")

# Lottie Animation
import requests
from streamlit_lottie import st_lottie
lottie = requests.get("https://assets5.lottiefiles.com/packages/lf20_V9t630.json").json()
st_lottie(lottie, height=150)
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #E8EAF6, #FFF); }
[data-testid="stSidebar"] { background-color: #F0F2F6; }
h2 { color: #1E1E2F !important; }
.stButton>button { background-color: #1E1E2F; color: #FFF; border-radius:8px; }
</style>
""", unsafe_allow_html=True)
import streamlit as st
import yaml
import streamlit_authenticator as stauth

with open('config.yaml') as f:
    config = yaml.safe_load(f)

auth = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

login_result = auth.login(location='sidebar')
if not login_result:
    st.warning("Please enter your username and password")
else:
    name, status, username = login_result
    if status:
        auth.logout(location='sidebar')
        role = config['credentials']['usernames'][username]['roles'][0]

        st.markdown("<h2>3Knots Digital CEO Dashboard</h2>", unsafe_allow_html=True)
        st.write(f"**User:** {name} — Role: {role}")
        if role == 'admin':
            st.subheader("🔐 Admin Panel")
        st.subheader("📊 Dashboard Overview")
    elif status is False:
        st.error("Username/password incorrect")
    else:
        st.warning("Please enter credentials")
