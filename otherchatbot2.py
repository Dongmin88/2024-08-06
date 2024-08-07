from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))

def analyze_conversation(query):
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            }
        )
    return result['result']['prediction']['topIntent']

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "안녕": "안녕하세요! 만나서 반가워요.",
            "이름이 뭐야?": f"제 이름은 {self.name}입니다.",
            "어떻게 지내?": "저는 항상 잘 지내고 있어요. 당신은 어떻게 지내시나요?",
            "잘 가": "안녕히 가세요! 또 만나요.",
        }

    def get_response(self, user_input):
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            intent = analyze_conversation(user_input)
            if intent == "SendEmail":
                return "네 지금 메일 보내겠습니다."
            else:
                return "죄송해요, 이해하지 못했어요."

def main():
    bot_name = "ChatGPT"
    chatbot = ChatBot(bot_name)
    print(f"안녕하세요! 저는 {chatbot.name} 챗봇입니다. 무엇을 도와드릴까요?")

    while True:
        user_input = input("You: ")
        print(f"You: {user_input}")
        if user_input == "종료":
            print("ChatBot: 안녕히 가세요!")
            break
        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()