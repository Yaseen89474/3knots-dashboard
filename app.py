import streamlit as st
import yaml
import streamlit_authenticator as stauth

# Load config
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Hash plain-text passwords once
hashed = stauth.Hasher(
    [u["password"] for u in config["credentials"]["usernames"].values()]
).generate()
for i, u in enumerate(config["credentials"]["usernames"]):
    config["credentials"]["usernames"][u]["password"] = hashed[i]

auth = stauth.Authenticate(
    config['credentials'], config['cookie']['name'],
    config['cookie']['key'], config['cookie']['expiry_days'],
    config.get('preauthorized')
)

name, status, username = auth.login('Login', 'sidebar')
if status:
    auth.logout('Logout', 'sidebar')
    role = config['credentials']['usernames'][username]['roles'][0]
    st.markdown(
        "<div style='background:#1E1E2F;padding:15px;border-radius:8px'>"
        "<h2 style='color:#fff;text-align:center;'>3Knots Digital CEO Dashboard</h2></div>",
        unsafe_allow_html=True
    )
    st.write(f"**User:** {name} — Role: {role}")
    if role == 'admin':
        st.subheader("🔐 Admin Panel")
        st.write("Here you can manage user access etc.")
    st.subheader("📊 Dashboard Overview")
    st.write("Sales, Marketing, Projects placeholders...")
elif status is False:
    st.error("Username/password incorrect")
else:
    st.warning("Please enter credentials")
