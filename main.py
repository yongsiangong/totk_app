import pandas as pd
import streamlit as st

st.title("The Legend of Zelda: Tears of the Kingdom Shrine Walkthrough")

@st.cache_resource
def show_maps(sky_or_surface):
    if sky_or_surface == "Surface":
        st.write("- Surface Map:")
        st.image("shrine_surface.png")
    if sky_or_surface == "Sky":
        st.write("- Sky Map:")
        st.image("shrine_sky.png")

sky_or_surface = st.selectbox("Select surface or sky map", options = ['None', 'Surface', "Sky"])
show_maps(sky_or_surface)

df = pd.read_excel('shrine_url.xlsx')
list_of_shrines = list(df['shrine'].values)
list_of_shrines.sort()
shrine_url_dict = dict(zip(df['shrine'].values, df['url'].values))
shrine_yt_dict = dict(zip(df['shrine'].values, df['Youtube'].values))

shrines_selected = st.multiselect("Select shrine(s):", options = list_of_shrines)
if shrines_selected:
    for shrine in shrines_selected:
        st.subheader(shrine)
        st.write(f"- Guide: {shrine_url_dict.get(shrine)}")
        st.write("- YouTube Walkthrough:")
        st.video(shrine_yt_dict.get(shrine))
        st.write("----")