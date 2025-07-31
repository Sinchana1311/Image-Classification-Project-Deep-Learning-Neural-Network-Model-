Image Classification Using Deep Learning

Introduction

The Image Classification Web App is a deep learning-based application developed using TensorFlow, Keras, and Streamlit. This web app allows users to upload an image of a fruit or vegetable and receive an instant prediction about the category of the item. It demonstrates how machine learning models can be integrated into interactive web applications for real-time inference. This project showcases the use of Convolutional Neural Networks (CNNs) for multi-class image classification and presents the results through a user-friendly interface.

Objective

The primary goal of this project is to create a robust image classification model that can accurately classify images into different categories of fruits and vegetables. The model is deployed in a Streamlit web app, making it accessible to users without coding knowledge. The project highlights the integration of machine learning with web technologies.

Features

- Image upload functionality through a web interface
- Deep learning-based prediction using a trained CNN model
- Displays the predicted class and confidence score
- Image preview for user confirmation
- Runs locally with a simple command

Technologies Used

Frontend (via Streamlit):
- Streamlit components for layout and user interaction
- Real-time image display and output

Backend:
- Python 3.x
- TensorFlow 2.x
- Keras (for model creation and loading)
- NumPy (for preprocessing image data)

Implementation Details

Model:
- Convolutional Neural Network (CNN)
- Input size: 180x180 pixels
- Output: 36-class softmax probability distribution
- Trained on a dataset of fruits and vegetables
- Saved in `.keras` format using `model.save()`

Streamlit Web App:
- Loads and preprocesses the uploaded image
- Predicts using the loaded model
- Displays both the prediction label and confidence score

How to Run the Project

1. Ensure Python is installed

   Recommended version: Python 3.10 or 3.11

2. Create and activate a virtual environment

   On Windows:
   python -m venv venv
   venv\Scripts\activate

   On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies

   If `requirements.txt` is present:
   pip install -r requirements.txt
     Or manually:
   pip install tensorflow streamlit numpy

4. Run the Streamlit application
   streamlit run app.py
   
5. Open your browser
   Go to: http://localhost:8501

Classes Used for Prediction

The model is trained on 36 fruit and vegetable categories including:

apple, banana, beetroot, bell pepper, cabbage, capsicum, carrot, cauliflower, chilli pepper, corn, cucumber, eggplant, garlic, ginger, grapes, jalapeno, kiwi, lemon, lettuce, mango, onion, orange, paprika, pear, peas, pineapple, pomegranate, potato, radish, soy beans, spinach, sweetcorn, sweetpotato, tomato, turnip, and watermelon.

Conclusion

This Image Classification Web App demonstrates how deep learning can be applied to real-world problems using a clean and interactive web interface. By leveraging TensorFlow and Streamlit, the project provides a complete pipeline from model training to deployment. It can serve as a template for other image-based machine learning applications and can be further extended with additional features such as real-time video input or mobile integration.


