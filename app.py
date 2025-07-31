import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
import streamlit as st
import numpy as np

st.header('🍎🥕 Image Classification Model')

# 1. Load the model
try:
    model = load_model(r'C:\Python\Image_Classification\Image_classify.keras')
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# 2. Define classes
data_cat = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum',
    'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant',
    'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce',
    'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple',
    'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn',
    'sweetpotato', 'tomato', 'turnip', 'watermelon'
]

# 3. Image upload
uploaded_file = st.file_uploader("📤 Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img_height, img_width = 180, 180
    image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
    st.image(image, caption="Uploaded Image", width=200)

    img_array = img_to_array(image)
    img_batch = tf.expand_dims(img_array, 0)

    # 4. Predict
    prediction = model.predict(img_batch)
    score = tf.nn.softmax(prediction[0])

    st.write(f"✅ Prediction: **{data_cat[np.argmax(score)]}**")
    st.write(f"🔍 Confidence: **{round(100 * np.max(score), 2)}%**")
