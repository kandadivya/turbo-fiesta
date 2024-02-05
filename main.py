import os
import streamlit as st
import cv2
import numpy as np

st.title('Change the color of your signature!')
uploaded_file = st.file_uploader("Choose a image file", type=["jpg", "png", "jpeg"])# this is the widget to get

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("Display window", img)
    # k = cv2.waitKey(0)

    ret, thresh = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

    ##cv2.imshow("binary", thresh)

    rgba = cv2.cvtColor(thresh, cv2.COLOR_RGB2RGBA)

    # this runs through the array
    for y in range(rgba.shape[0]):
        for x in range(rgba.shape[1]):
            if np.all(rgba[y, x] == [255, 255, 255, 255]):  # check if pixel is white
                rgba[y, x, 3] = 0  # sets alpha channel to 0 for the white ones



    path = "C:\\Users\\Divya\\Desktop\\pleasework"
    cv2.imwrite(os.path.join(path, 'image.png'), rgba)




    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    if col1.button('Blue'):
        for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]):  # check if pixel is black
                    # Set the pixel to blue
                    rgba[y, x] = [0, 0, 255, 255]
    if col2.button('Red'):
        for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]):  # check if pixel is black
                    # Set the pixel to red
                    rgba[y, x] = [255, 0, 0, 255]

    if col3.button('Green'):
        for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]):  # check if pixel is black
                    # Set the pixel to green
                    rgba[y, x] = [0, 255, 0, 255]

    if col4.button('Pink'):
        for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]):  # check if pixel is black
                    # Set the pixel to green
                    rgba[y, x] = [222, 49, 99, 255]

    if col5.button('Purple'):
        for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]):  # check if pixel is black
                    # Set the pixel to green
                    rgba[y, x] = [207, 159, 225, 255]

    st.write('Try a new color')

    red = st.slider('Red', 0, 255, 0)
    green = st.slider('Green', 0, 255, 0)
    blue = st.slider('Blue', 0, 255, 0)

    for y in range(rgba.shape[0]):
            for x in range(rgba.shape[1]):
                 if np.all(rgba[y, x] == [0, 0, 0, 255]) and (red != 0 or green != 0 or blue != 0):
                    # Set the pixel to green
                    rgba[y, x] = [red, green, blue, 255]

    st.image(rgba, caption='This is your image!')

else:
    st.write("Please upload an image file.")

