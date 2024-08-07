# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
key = '09de982ff646430880d5102a5565e183'
endpoint = 'https://b03-lang6.cognitiveservices.azure.com'

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction,AbstractiveSummaryAction
        
    ) 

    document = [
        "추출 요약 기능은 자연어 처리 기술을 사용하여 비정형 텍스트 문서에서 주요 문장을 찾아냅니다. "
        "이러한 문장들은 문서의 주요 아이디어를 집합적으로 전달합니다. 이 기능은 개발자들에게 API로 제공됩니다. "
        "개발자들은 이를 사용하여 다양한 사용 사례를 지원하기 위해 관련 정보를 기반으로 한 지능형 솔루션을 구축할 수 있습니다. "
        "추출 요약은 여러 언어를 지원합니다. 이는 사전 학습된 다국어 변환기 모델을 기반으로 하며, 전체적인 표현을 추구하는 우리의 노력의 일환입니다. "
        "이는 단일 언어 간의 전이 학습에서 힘을 얻어 언어의 공통된 특성을 활용하여 개선된 품질과 효율성을 가진 모델을 생성합니다."
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
        language='ko'
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )
    
    poller = client.begin_analyze_actions(
        document,
        actions=[AbstractiveSummaryAction(sentence_count=2)],
        language='ko'
    )

    document_results = poller.result()
    for result in document_results:
        abstractive_summary_result = result[0]  # first document, first result
        if abstractive_summary_result.is_error:
            print(f"Error: {abstractive_summary_result.code} - {abstractive_summary_result.message}")
        else:
            print("summary Abstractived: \n{}".format(
                " ".join([summary.text for summary in abstractive_summary_result.summaries])
            ))

sample_extractive_summarization(client)