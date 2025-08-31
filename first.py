import streamlit as st
import yt_dlp
import os

def downloadVideo(url, save_path):
    # Ensure save path ends with a slash if it's a folder
    if os.path.isdir(save_path):
        output_template = os.path.join(save_path, '%(title)s.%(ext)s')
    else:
        # If a file path is given instead of a folder
        output_template = save_path

    st.success(f"Downloading started for: {url}")
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_template,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.success(f"Video downloaded to: `{output_template}`")
    except Exception as e:
        st.error(f"Error during download: {e}")

# UI
st.title('Softcrayons - YouTube Video Downloader')

video_link = st.text_input("📽️ Enter Video URL", placeholder="Paste your YouTube video URL here")

# Ask user where to save the video
save_location = st.text_input("📁 Enter Save Location", placeholder="e.g. downloads/ or downloads/myvideo.mp4")

if st.button("Download"):
    if not video_link.strip():
        st.warning("⚠️ Please enter a valid video URL.")
    elif not save_location.strip():
        st.warning("⚠️ Please enter a valid save location.")
    else:
        downloadVideo(video_link, save_location)



# import streamlit as st
# import yt_dlp
# import os




# def   downloadVideo(url):
#      st.success(f"Downloading started for: {url}")
#      ydl_opts = {'format': 'best'}

#      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#         st.success("Video Downloaded")
      

# st.title('Softcrayons')
# # st.write("Hello! This is running in your browser.")
# input_warning="Video Url"
# video_link = st.text_input(input_warning, placeholder="Copy Your Url here ")





# if st.button("download"):
#      if  video_link.strip():
#         downloadVideo(video_link)
#      else:
#          st.warning("Invalid Url")


