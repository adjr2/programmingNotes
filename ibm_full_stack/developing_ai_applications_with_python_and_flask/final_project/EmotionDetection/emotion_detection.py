import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=obj, headers=headers)
    formatted_response = json.loads(response.text)
    res = formatted_response["emotionPredictions"][0]["emotion"]
    res["dominant_emotion"] = [k for k, v in res.items() if v == max(res.values())][0]
    
    return res