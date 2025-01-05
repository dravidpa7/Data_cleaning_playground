import streamlit as st
pg=st.navigation([st.Page("cleaning.py"),st.Page("improve.py"),st.Page("information.py"),st.Page("ploting.py"),st.Page("Developer.py")])
pg.run()
