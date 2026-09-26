import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion_detector service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Check if the response status code is 200 (Successful)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # 2. Extract the required set of emotions and their scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # 3. Write code logic to find the dominant emotion (highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # 4. Return the required output format dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    # If the response status code is 400 (Bad Request / Blank entry), return dictionary with None values
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }