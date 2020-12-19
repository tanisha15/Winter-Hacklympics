import cv2
import streamlit as st
from videostabilizer import VideoStabilizer

video = cv2.VideoCapture(r"C:\Users\tanis\Desktop\bolt.mp4")
stabilizer = VideoStabilizer(video)

while True:
	success, _, frame = stabilizer.read()
	if not success:
		print("No frame is captured.")
		break
		
	cv2.imshow("Stabilized Video", frame)
	if cv2.waitKey(20) == 27:
		break

def main():
    """Face Recognition App"""

    st.title("STABLYMPIC WEB APP")

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Video Stabilization WebApp</h2>
    </div>
    </body>
     """
    
    st.markdown(html_temp, unsafe_allow_html=True)

    with open(r"C:\Users\tanis\Desktop\bolt.mp4",'rb') as v:
        st.text("Original video")
        st.video(v)

    if st.button("Stabilize"):
         with open(r"C:\Users\tanis\Desktop\boltoutput.mp4",'rb') as out:
             st.text("Stabilized Video")
             st.video(out)

if __name__ == '__main__':
    main()



