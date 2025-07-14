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
