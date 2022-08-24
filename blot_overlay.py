import streamlit as st
import numpy as np
from tifffile import imread
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
"""
# Easy Blot Overlay

You can use this to overlay a digitized image of a western blot with the ECL images of that blot. You can stick it in any colour you want, I hope!

Let me know if there are any problems
"""
dig_image = st.file_uploader('Image of blot')

red_bytes = st.file_uploader('Red Channel')
green_bytes = st.file_uploader('Green Channel')
blue_bytes = st.file_uploader('Blue Channel')

def normalize(image):
    return image/np.max(image)


if dig_image is not None:
    digitized = imread(dig_image)
    norm_dig = normalize(digitized)
    dig_3_ch = normalize(np.array([digitized]*3).transpose((1,2,0)))
    if red_bytes is not None:
        red = imread(red_bytes)

        norm_red = normalize(red)
        comp_red = norm_dig+norm_red

        dig_3_ch[:,:,0] = comp_red
        dig_3_ch = normalize(dig_3_ch)

    if green_bytes is not None:
        green = imread(green_bytes)

        
        norm_green = normalize(green)
        comp_green = norm_dig+norm_green

        dig_3_ch[:,:,1] = comp_green
        dig_3_ch = normalize(dig_3_ch)

    if blue_bytes is not None:
        blue = imread(blue_bytes)

        
        norm_blue = normalize(blue)
        comp_blue = norm_dig+norm_blue

        dig_3_ch[:,:,2] = comp_blue
        dig_3_ch = normalize(dig_3_ch)

    st.image(dig_3_ch, clamp = True)

    #result = Image.fromarray(dig_3_ch.astype('uint8'), 'RGB')
    #buf = BytesIO()
    #img = Image.open(result)
    #img.save(buf, format='png')
    #byte_im = buf.getvalue()

    #btn = st.download_button(
    #    label = 'Download Composite',
    #    data = byte_im,
    #    filename = 'composite.png',
    #    mime = 'image/png'
    #)