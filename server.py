"""
This module is a Flask web application for Emotion Detection.
It handles user requests and renders the emotion analysis results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialise the Flask app named "Emotion Detector"
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function retrieves text from the request arguments,
    passes it to the emotion_detector function, and returns the result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the individual emotion scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None, indicating an error or invalid/blank input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with all emotion scores and the dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    This function renders the main application index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    