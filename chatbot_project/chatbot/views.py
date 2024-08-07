from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            bot_response = generate_response(user_message)
            return JsonResponse({'response': bot_response})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

def generate_response(message):
    if '안녕' in message:
        return '안녕하세요! 무엇을 도와드릴까요?'
    elif '날씨' in message:
        return '오늘의 날씨는 맑습니다.'
    else:
        return '죄송합니다, 이해하지 못했습니다.'
