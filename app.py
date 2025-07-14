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
    # 💡 Remove preauthorized! It is no longer supported
)

name, status, username = auth.login('sidebar')  # only location required now

if status:
    auth.logout('sidebar')
    # ... rest of login logic ...
