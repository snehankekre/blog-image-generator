import streamlit as st
from slugify import slugify
from steps.step1 import step1
from steps.step2 import step2
from steps.step3 import step3

# Presentational content

st.markdown('<div style="font-size: 4rem; margin-bottom: -3rem;">🎨</div>', unsafe_allow_html=True)

'''
# Blog image generator

An app to generate good-looking images for [our blog](https://blog.streamlit.io).
'''

'---'

def reset_images():
    if 'images' in st.session_state:
        del st.session_state.images

template = step1(on_template_changed=reset_images)

if not template:
    st.stop()

'---'

out = step2(template)

if not out:
    st.stop()

'---'

step3(out)
