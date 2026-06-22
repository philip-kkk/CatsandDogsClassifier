---

title: Cats and Dogs Classifier
sdk: gradio
app_file: app.py
python_version: "3.10"
----------------------

# Cats and Dogs Classifier

Cats and Dogs Classifier is a simple image classification web application that predicts whether an uploaded image is a cat or a dog.

The project is deployed using **Gradio** and is designed to run on **Hugging Face Spaces**. Users can upload an image through the interface, and the trained model will return the predicted class together with the probability scores.

---

## Demo

Upload an image of a cat or a dog, then wait for the model to return its prediction.

The output includes:

* Probability score for **Cat**
* Probability score for **Dog**
* Final predicted label

---

## Project Structure

The repository should keep the following structure:

```text
CatsandDogsClassifier/
│
├── README.md
├── app.py
├── cat_dog_model.keras
└── requirements.txt
```

### File Description

| File                  | Description                                                                        |
| --------------------- | ---------------------------------------------------------------------------------- |
| `README.md`           | Project description and Hugging Face Space configuration.                          |
| `app.py`              | Main Gradio application file. Hugging Face Spaces runs this file to start the app. |
| `cat_dog_model.keras` | Trained Keras model used for cat and dog classification.                           |
| `requirements.txt`    | Python dependencies required to run the app.                                       |

---

## How It Works

The application uses a trained TensorFlow/Keras model to classify uploaded images.

When a user uploads an image:

1. The image is converted to RGB format.
2. The image is resized to `200 x 200`.
3. The image is converted into a NumPy array.
4. The trained model predicts whether the image is more likely to be a cat or a dog.
5. The app returns both the probability scores and the final prediction.

The prediction rule is:

```text
If the model output is greater than or equal to 0.5, the image is predicted as Dog.
Otherwise, the image is predicted as Cat.
```

---

## Requirements

The project uses the following main libraries:

```text
tensorflow-cpu
gradio
Pillow
numpy
```

These dependencies are listed in `requirements.txt`, so Hugging Face Spaces can install them automatically during deployment.

---

## Running Locally

You can also run the project on your local computer.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd CatsandDogsClassifier
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

After running the command, Gradio will provide a local link. Open the link in your browser and upload an image to test the classifier.

---

## Hugging Face Spaces Deployment Notes

This repository is prepared for Hugging Face Spaces deployment.

To avoid deployment errors, keep these files in the root folder:

```text
app.py
cat_dog_model.keras
requirements.txt
README.md
```

Important notes:

* Do not rename `app.py` unless you also update `app_file` in the README metadata.
* Do not rename `cat_dog_model.keras` unless you also update `MODEL_PATH` in `app.py`.
* Do not remove `requirements.txt`, because Hugging Face Spaces uses it to install the required Python libraries.
* Keep the YAML configuration block at the very top of `README.md`.
* The app currently uses CPU TensorFlow through `tensorflow-cpu`, so it can run on the default Hugging Face CPU environment.

---

## Model Information

The model is a trained Keras image classification model saved as:

```text
cat_dog_model.keras
```

The model takes an image resized to:

```text
200 x 200
```

and returns a binary prediction for:

```text
Cat / Dog
```

---

## Example Usage

1. Open the app.
2. Upload an image containing a cat or a dog.
3. Wait for the prediction result.
4. Check the probability scores and the final predicted label.

Example output:

```text
Dog: 0.87
Cat: 0.13
Prediction: Dog
```

---

## Common Problems

### 1. The app cannot find the model file

Make sure this file exists in the root folder:

```text
cat_dog_model.keras
```

If the file is renamed or moved, update the model path inside `app.py`.

---

### 2. Hugging Face Space shows a build error

Check that:

* `requirements.txt` exists.
* `app.py` exists in the root folder.
* The YAML block at the top of `README.md` is valid.
* `app_file: app.py` matches the actual application file name.

---

### 3. Local Python version issue

This Space is configured to use:

```text
Python 3.10
```

If running locally, using Python 3.10 is recommended to match the Hugging Face environment.

---

## Future Improvements

Possible improvements for the project:

* Add more details about the training dataset.
* Add model accuracy and evaluation results.
* Add example test images.
* Improve the user interface layout.
* Add confidence-based messages for uncertain predictions.

---

## Author

Created by Philip.

---

## Acknowledgements

This project uses:

* TensorFlow/Keras for the trained classification model.
* Gradio for the web interface.
* Hugging Face Spaces for public deployment.
