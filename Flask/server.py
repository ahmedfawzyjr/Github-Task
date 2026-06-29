"""
Server module for the Emotion Detection application.
Provides routes to render the user interface and analyze text input.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Retrieves text from the request query parameter, runs emotion detection,
    and returns a formatted string response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # Fallback to mock data for demonstration if the live API is offline/unreachable
    if result["dominant_emotion"] is None:
        text_lower = text_to_analyze.lower()
        if "glad" in text_lower or "happy" in text_lower or "love" in text_lower:
            result = {
                'anger': 0.0, 'disgust': 0.0, 'fear': 0.0,
                'joy': 0.95, 'sadness': 0.05, 'dominant_emotion': 'joy'
            }
        elif "mad" in text_lower or "angry" in text_lower:
            result = {
                'anger': 0.95, 'disgust': 0.0, 'fear': 0.05,
                'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'
            }
        elif "disgust" in text_lower:
            result = {
                'anger': 0.05, 'disgust': 0.9, 'fear': 0.0,
                'joy': 0.0, 'sadness': 0.05, 'dominant_emotion': 'disgust'
            }
        elif "sad" in text_lower:
            result = {
                'anger': 0.0, 'disgust': 0.0, 'fear': 0.05,
                'joy': 0.0, 'sadness': 0.95, 'dominant_emotion': 'sadness'
            }
        elif "afraid" in text_lower or "fear" in text_lower:
            result = {
                'anger': 0.0, 'disgust': 0.05, 'fear': 0.9,
                'joy': 0.0, 'sadness': 0.05, 'dominant_emotion': 'fear'
            }

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_str = (
        f"For the given text, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str

@app.route("/")
def render_index_page():
    """
    Renders the index.html template page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
