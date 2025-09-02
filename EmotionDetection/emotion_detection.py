# Import libraries
import requests
import json

def emotion_detector(text_to_analyse):
    """ Function to detect the emotion of a text
    Args: 
        - text_to_analyse: String of text
    Returns:
        - emotions: The emotion set with the dominant value
    """
    # Link to access watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers send to watson
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Payload
    myobj =  { "raw_document": { "text": text_to_analyse } }
    # Send post to watson
    response = requests.post(url, json=myobj, headers=header)
    # Check status_code
    if response.status_code == 400:
        return {"anger":None,
        "joy":None,
        "disgust":None,
        "fear":None,
        "sadness":None,
        "dominant_emotion":None}
    else:
        # Access the response text in json
        json_text = json.loads(response.text)
        # Emotion extractor
        emotions = json_text["emotionPredictions"][0]["emotion"]
        # Dominant emotion finder
        dominant_emotion = max(emotions.items(), key = lambda emotions: emotions[1])
        # Join the dictionaries
        emotions["dominant_emotion"] = dominant_emotion[0]
        return emotions