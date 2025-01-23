import streamlit as st
import pickle
import gzip
import numpy as np
from PIL import Image

# Load the compressed RandomForestClassifier model
with gzip.open('rfc.pkl.gz', 'rb') as f:
    rfc = pickle.load(f)

# Creating the web app
st.title('Forest Cover Type Prediction')
image = Image.open('img.png')
st.image(image, caption='Forest Cover Type', use_column_width=True)

# Get user input for features
user_input = st.text_input('Enter Features (comma-separated values)')

if user_input:
    try:
        # Process user input
        user_input = user_input.split(',')
        features = np.array([user_input], dtype=np.float64)

        # Make prediction
        output = rfc.predict(features).reshape(1, -1)

        # Define the cover type dictionary
        cover_type_dict = {
            1: {"name": "Spruce/Fir", "image": "img_1.png"},
            2: {"name": "Lodgepole Pine", "image": "img_2.png"},
            3: {"name": "Ponderosa Pine", "image": "img_3.png"},
            4: {"name": "Cottonwood/Willow", "image": "img_4.png"},
            5: {"name": "Aspen", "image": "img_5.png"},
            6: {"name": "Douglas-fir", "image": "img_6.png"},
            7: {"name": "Krummholz", "image": "img_7.png"}
        }

        # Convert output to integer
        predicted_cover_type = int(output[0])
        cover_type_info = cover_type_dict.get(predicted_cover_type)

        if cover_type_info:
            cover_type_name = cover_type_info["name"]
            cover_type_image_path = cover_type_info["image"]

            # Display cover type information
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write("Predicted Cover Type:")
                st.write(f"<h1 style='font-size: 40px; font-weight: bold;'>{cover_type_name}</h1>", unsafe_allow_html=True)
            with col2:
                cover_type_image = Image.open(cover_type_image_path)
                st.image(cover_type_image, caption=cover_type_name, use_column_width=True)
        else:
            st.error("Unable to make a prediction. Cover type not found.")
    except ValueError:
        st.error("Invalid input! Please enter numerical values separated by commas.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
