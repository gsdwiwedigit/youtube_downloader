import streamlit as st
import yt_dlp



def   downloadVideo(url):
     st.success(f"Downloading started for: {url}")
     ydl_opts = {'format': 'best'}

     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        st.success("Video Downloaded")
      

st.title('Softcrayons')
# st.write("Hello! This is running in your browser.")
input_warning="Video Url"
video_link = st.text_input(input_warning, placeholder="Copy Your Url here ")





if st.button("download"):
     if  video_link.strip():
        downloadVideo(video_link)
     else:
         st.warning("Invalid Url")


