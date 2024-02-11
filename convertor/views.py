from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

class LanguageCovertorView(View):
    TEMPLATE_NAME = 'landing/language_convertor.html'

    def get(self, request, *args, **kwargs):
            
        context = {}

        return render(request, self.TEMPLATE_NAME, context)
    
    def post(self, request, *args, **kwargs):

        fromText = request.POST.get("fromText")
        fromLanguage = request.POST.get("fromLanguage")
        toLanguage = request.POST.get("toLanguage")

        prompt = f"translate and return the answer into {toLanguage}: {fromText}"
        desire_output = f"You are a helpful language translator that can convert the given input text or sentence which is in language {fromLanguage} and returns after translate it into {toLanguage}"
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [
            {"role":"system","content":desire_output},
            {"role":"user","content":prompt},
            
            ],
            n=1,
            temperature = 0.1
        )

        translation_result = response.choices[0].message.content

        context = {
            "data":translation_result
        }

        return JsonResponse(context)


