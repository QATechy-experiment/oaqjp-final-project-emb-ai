from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialise the Flask app named "Emotion Detector"
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
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
    
    # Return a formatted string with all emotion scores and the dominant emotion
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is <b>{}</b>.".format(
        anger, disgust, fear, joy, sadness, dominant_emotion
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)