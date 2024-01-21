import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#MainMenu {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.title(":bar_chart: Flujo de caja")
