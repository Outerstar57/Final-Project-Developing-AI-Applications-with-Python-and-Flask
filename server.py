"""
This file purpose is to handle the Flask app
"""
# Libraries
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Start app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def send_text():
    """
    Function that sends the text
    """
    # Get the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')
    # Get the emotions
    response = emotion_detector(text_to_analyze)
    # Check the response of the function
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # Else
    return f"""For the given statement, the system response is
    'anger': {response["anger"]},
    'disgust': {response["disgust"]},
    'fear': {response["fear"]},
    'joy': {response["joy"]} and
    'sadness': {response["sadness"]}.
    The dominant emotion is {response["dominant_emotion"]}."""

@app.route("/")
def render_index_page():
    """
    Renders index page
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
