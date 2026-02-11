import gradio as gr
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = 'cat_dog_model.keras'
IMG_SIZE = (200, 200)

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(img: Image):
    img = img.convert('RGB').resize(IMG_SIZE)
    
    x = np.array(img, dtype=np.float32)
    x = np.expand_dims(x, axis=0)
    
    predictions = float(model.predict(x, verbose=0)[0][0])
    label = "Dog" if predictions >= 0.5 else "Cat"
    return {"Dog": predictions, "Cat": 1.0 - predictions}, label

demo = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Upload an image"),
    outputs=[gr.Label(num_top_classes=2, label="Probabilities"), gr.Textbox(label="Predictions")],
    title="Cat vs Dog Classifier",
    description="Upload an image and get a prediction if it is a cat or dog."
)

if __name__ == "__main__":
    demo.launch()