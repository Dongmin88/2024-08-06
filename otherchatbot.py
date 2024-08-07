while True:
    client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
    
    with client:
        query = input("put your conversation.")
        print(f"You: {query}")
        
        if query == "exit":
            print("Bot: 다음에봐~")
            break
        
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

    topIntent = result['result']['prediction']['topIntent']
    bot = {"SendEmail": "이메일 안본다 연락해~", "Welcome": "그래 나도 반갑다.", "Delete": "헉! 다 지워버림"}.get(topIntent, f"나머지는 아직 등록 안됐다. {topIntent}")
    