import streamlit as st
import yaml
from streamlit_authenticator.utilities.hasher import Hasher
import streamlit_authenticator as stauth

with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Fix hashing
passwords = [u["password"] for u in config["credentials"]["usernames"].values()]
hashed = Hasher(passwords).generate()
for i, user in enumerate(config["credentials"]["usernames"]):
    config["credentials"]["usernames"][user]["password"] = hashed[i]

auth = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config.get('preauthorized')
)
