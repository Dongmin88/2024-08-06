import os
import requests
import json
import time
 
def recognize_custom_entities():
    # 샘플을 실행하기 전에 환경 변수를 자신의 값으로 설정합니다.
    endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT", "https://fletaaiservicesgroup.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview")
    subscription_key = os.getenv("AZURE_LANGUAGE_KEY", "e2895d88fc1445baa39a971e40c3c17d")
    project_name = os.getenv("CUSTOM_ENTITIES_PROJECT_NAME", "customnerdomo")
    deployment_name = os.getenv("CUSTOM_ENTITIES_DEPLOYMENT_NAME", "cnerdendeply")
    path_to_sample_document = "Test 1.txt"
 
    # 문서를 읽습니다.
    with open(path_to_sample_document, 'r') as file:
        document_text = file.read()
 
    # 요청 페이로드를 준비합니다.
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
                    "language": "en"  # 문서의 언어가 다르면 여기를 변경하세요.
                }
            ]
        }
    }
 
    # 헤더를 설정합니다.
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
 
    # 요청을 보냅니다.
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
 
    if response.status_code == 202:
        operation_location = response.headers["operation-location"]
        print(f"작업이 수락되었습니다. 상태를 확인하기 위해 {operation_location}을(를) 주기적으로 확인하십시오.")
 
        # 주기적으로 상태를 확인하여 작업이 완료될 때까지 대기합니다.
        while True:
            status_response = requests.get(operation_location, headers=headers)
            status_result = status_response.json()
 
            if status_response.status_code != 200:
                print(f"상태 확인 오류: {status_response.status_code} - {status_response.text}")
                break
 
            if status_result["status"] == "succeeded":
                print("사용자 정의 엔터티 인식 결과:")
                for task in status_result['tasks']['items']:
                    if task['status'] == 'succeeded':
                        for entity_result in task['results']['documents']:
                            for entity in entity_result['entities']:
                                print(f"엔터티 '{entity['text']}'는 카테고리 '{entity['category']}'를 가지며 신뢰 점수는 '{entity['confidenceScore']}'입니다.")
                    else:
                        print(f"작업 실패, 오류: {task['results']['errors']}")
                break
            elif status_result["status"] == "failed":
                print(f"작업 실패: {status_result}")
                break
            else:
                print(f"작업 상태: {status_result['status']}... 대기 중...")
                time.sleep(5)  # 5초 대기 후 상태를 다시 확인합니다.
    else:
        print(f"오류: {response.status_code} - {response.text}")
 
if __name__ == "__main__":
    recognize_custom_entities()