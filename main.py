import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.set_page_config(page_title="Flujo de caja", page_icon=":bar_chart:", layout="wide")
