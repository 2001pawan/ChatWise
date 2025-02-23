from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            ai_response = response.choices[0].message.content
            return JsonResponse({'response': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'chat/chat.html')
