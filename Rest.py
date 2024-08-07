import requests
import json
import time

# Azure Cognitive Services endpoint and subscription key
endpoint = 'https://b03-lang6.cognitiveservices.azure.com/'
key = '09de982ff646430880d5102a5565e183'
project_name = 'customnerdemo'
deployment_name = 'cnerdemodeply'

# Document file path
path_to_sample_document = './Test 1.txt'

# Read the content of the document
with open(path_to_sample_document, 'r', encoding='utf-8') as file:
    document_text = file.read()

# REST API request URL
url = f"{endpoint}/language/analyze-text/jobs?api-version=2022-10-01-preview"

# Headers for the API request
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-Type': 'application/json'
}

# Request payload
payload = {
    "tasks": [
        {
            "kind": "CustomEntityRecognition",
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name,
                "stringIndexType": "TextElement_v8"
            }
        }
    ],
    "displayName": "CustomTextPortal_CustomEntityRecognition",
    "analysisInput": {
        "documents": [
            {
                "id": "document_CustomEntityRecognition",
                "text": document_text,
                "language": "en"  # Adjust the language code if necessary
            }
        ]
    }
}

# Make the API request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check for errors
if response.status_code != 202:
    print(f"Error: {response.status_code}")
    print(response.json())
else:
    print("Job created successfully.")
    # Retrieve the operation location from the response headers
    operation_location = response.headers['Operation-Location']

    # Poll the operation location until the job is complete
    job_complete = False
    while not job_complete:
        job_response = requests.get(operation_location, headers=headers)
        job_status = job_response.json()

        if job_status['status'] in ['succeeded', 'failed']:
            job_complete = True
        else:
            print("Job is still running...")
            time.sleep(5)  # Wait for 5 seconds before polling again

    # Print the results
    if job_status['status'] == 'succeeded':
        print("Job completed successfully.")
        results = job_status['tasks']['items'][0]['results']['documents']
        for result in results:
            for entity in result['entities']:
                print(f"Entity '{entity['text']}' has category '{entity['category']}' with confidence score of '{entity['confidenceScore']}'")
    else:
        print("Job failed.")
        print(job_status)
