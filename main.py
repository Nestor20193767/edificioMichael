import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
<style>
#MainMenu {
  visibility: hidden;
}
footer {
  visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.title(":bar_chart: Flujo de caja")
