import streamlit as st
import yaml
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Hash all plain-text passwords (new method)
config['credentials'] = Hasher.hash_passwords(config['credentials'])

auth = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config.get('preauthorized')
)

name, status, username = auth.login('Login', 'sidebar')
if status:
    auth.logout('Logout', 'sidebar')
    role = config['credentials']['usernames'][username]['roles'][0]

    st.markdown(… # your styling here
    )
