
import requests
import os

#Construct URL
endpoint = "https://b03-ai-services2.openai.azure.com/"
path = "/translator/document:translate"
url = endpoint + path

headers = {
    "Ocp-Apim-Subscription-Key": "d105c39d29d342c78a70536e475dc8e3"
}

# Define the parameters 
# Get list of supported languages and code here: https://aka.ms/TranslatorLanguageCodes 
params = {
    "sourceLanguage": "en",
    "targetLanguage": "ko",
    "api-version": "2023-11-01-preview"
}

# Include full path, file name and extension
input_file = "PowerPointSample.pptx"
output_file = "ko1-PowerPointSample.pptx"

# Open the input file in binary mode
with open(input_file, "rb") as document:
    # Define the data to be sent
    # Find list of supported content types here: https://aka.ms/dtsync-content-type
    data = {
        "document": (os.path.basename(input_file), document, "application/vnd.openxmlformats-officedocument.presentationml.presentation")
    }

    # Send the POST request
    response = requests.post(url, headers=headers, files=data, params=params)

# Write the response content to a file
with open(output_file, "wb") as output_document:
    output_document.write(response.content)
    
  
    