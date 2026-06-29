# Emotion Detection Web Application

An AI-powered web application that analyzes the emotional tone of text input using IBM Watson's Natural Language Processing (NLP) Emotion Predict service.

## Project Description
This project is built using the Flask web framework in Python and integrates Watson NLP models to detect major emotional categories in text, including:
- Joy
- Anger
- Disgust
- Sadness
- Fear

The backend identifies the scores for each emotion and computes the dominant emotion. Built-in error handling is implemented to gracefully catch invalid or blank inputs.

## Project Structure
- `EmotionDetection/`: Python package housing the core API logic.
  - `__init__.py`: Package initialization and function exposure.
  - `emotion_detection.py`: Service client function sending POST requests to Watson NLP.
- `server.py`: Flask application server that defines the web API and UI routes.
- `templates/`: Directory containing front-end templates (`index.html`).
- `static/`: Contains client-side JavaScript (`mywebscript.js`).
- `test_emotion_detection.py`: Test suite validating emotion detection accuracy.

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask requests pylint
   ```

## Running the Application
To run the server:
```bash
python server.py
```
Open a browser and navigate to `http://localhost:5000` to interact with the application.

## Running Unit Tests
To execute the test suite:
```bash
python test_emotion_detection.py
```
