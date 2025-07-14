import streamlit as st
import yaml
import streamlit_authenticator as stauth

# Load config
with open('config.yaml') as f:
    config = yaml.safe_load(f)

auth = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config.get('preauthorized'),
    auto_hash=True   # Let it automatically hash your passwords
)

name, status, username = auth.login('Login', 'sidebar')
if status:
    auth.logout('Logout', 'sidebar')
    role = config['credentials']['usernames'][username]['roles'][0]
    st.markdown(
        "<h2>3Knots Digital CEO Dashboard</h2>", unsafe_allow_html=True)
    st.write(f"**User:** {name} — Role: {role}")
    if role == 'admin':
        st.subheader("🔐 Admin Panel")
        st.write("Admin features here.")
    st.subheader("📊 Dashboard Overview")
    st.write("Your modules…")
elif status is False:
    st.error("Username/password incorrect")
else:
    st.warning("Please enter your credentials")
