import cv2
import streamlit as st

st.title("Test")
start = st.button('Start Video')

if start:

    streamlit_image = st.image([])
    video = cv2.VideoCapture("video/test-video.mp4")

    if not video.isOpened():
        st.error("Video is not opened!")
        st.stop()
    else:
        st.success("Video opened.")

    while True:

        check, frame = video.read()
        if not check or frame is None:
            st.error("Video finished!")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # cv2.putText(img=frame, text=datetime.now().strftime("%D - %A"), org=(30, 80),
        #             fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
        #             thickness=2, lineType=cv2.LINE_AA)

        # cv2.putText(img=frame, text=datetime.now().strftime("%I:%M:%S"), org=(30,140),
        #             fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,255,255),
        #             thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

    st.info("Video released successfully.")
