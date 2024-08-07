import requests, uuid, json

class Translator:
    def __init__(self):
        self.key = 'acfb449d53c0463fb28abb71bbeb8ac8'
        self.endpoint = "https://api.cognitive.microsofttranslator.com/"
        self.location = "australiaeast"
        self.path = '/translate'
        self.constructed_url = self.endpoint + self.path
    
    def translate(self, text, from_lang='en', to_lang='ko'):
        params = {
            'api-version': '3.0',
            'from': from_lang,
            'to': [to_lang]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{'text': text}]

        request = requests.post(self.constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        return response
    
    def pretty_print(self, response):
        print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    
    def get_translated_text(self, response):
        translated_text = response[0]['translations'][0]['text']
        return translated_text

# Usage example
if __name__ == "__main__":


    translator = Translator()
    text_to_translate = "I am so hungry. I want to have lunch time."
    response = translator.translate(text_to_translate)
    print(translator.get_translated_text(response))
