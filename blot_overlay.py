import streamlit as st
import numpy as np
from tifffile import imread
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

ch = st.selectbox('ECL colour', ['Red', 'Green', 'Blue'])

dig_image = st.file_uploader('Image of blot')

ecl_bytes = st.file_uploader('ECL image')
def normalize(image):
    return image/np.max(image)


if dig_image is not None:
    digitized = imread(dig_image)
    norm_dig = normalize(digitized)
    dig_3_ch = np.array([norm_dig]*3).transpose((1,2,0))
    if ecl_bytes is not None:
        ecl = imread(ecl_bytes)

        
        norm_ecl = normalize(ecl)
        comp_ecl = norm_dig+norm_ecl


        colour_channels = {'Red': 0, 'Green': 1, 'Blue': 2}

        dig_3_ch[:,:,colour_channels[ch]] = comp_ecl

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