import DALLE, asyncio
import streamlit as st
dalle = DALLE.DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
st.write("Generating images...")
images = await dalle.generate("Kitten")
