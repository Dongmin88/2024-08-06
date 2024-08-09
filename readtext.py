"""
This code sample shows Prebuilt Read operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient


class read_text:
    def __init__(self):
        self.key = "63f73bd764534768b7cd1968ca564f83"
        self.endpoint = "https://b03-docuintelli.cognitiveservices.azure.com/"


    def format_bounding_box(self, bounding_box):
        if not bounding_box:
            return "N/A"
        return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])

    def analyze_read(self,url):
        # sample document
        formUrl = url

        document_analysis_client = DocumentAnalysisClient(
            endpoint=self.endpoint, credential=AzureKeyCredential(self.key)
        )
        
        poller = document_analysis_client.begin_analyze_document_from_url(
                "prebuilt-read", formUrl)
        result = poller.result()

        print ("Document contains content: ", result.content)
        return result.content
        
