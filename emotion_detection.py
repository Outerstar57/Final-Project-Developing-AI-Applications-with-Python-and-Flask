# Import libraries
import requests

def emotion_detector(text_to_analyse):
    """ Function to detect the emotion of a text
    Args: 
        - text_to_analyse: String of text
    Returns:
        - text: The emotion
    """
    # Link to access watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers send to watson
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Payload
    myobj =  { "raw_document": { "text": text_to_analyse } }
    # Send post to watson
    response = requests.post(url, json=myobj, headers=header)
    # Access the response text
    text = response.text
    return text