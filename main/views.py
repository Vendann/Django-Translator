from django.shortcuts import render
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from os import remove, path

def index(request):
    if request.method == 'POST':
        if request.POST.get('translate'):
            lang = request.POST.get('lang')
            lang1, lang2 = lang.split(',')
            txt = request.POST.get('txt')

            translator = Translator()
            tr = translator.translate(txt, dest=lang1)

            if txt != '':
                speech = gTTS(text=str(tr.text), lang=str(lang2), tld='com')
                if path.isfile('speech.mp3'):
                    remove('speech.mp3')
                speech.save('speech.mp3')
            return render(request, 'main/index.html', {'result': tr.text})

        if request.POST.get('sound'):
            if path.isfile('speech.mp3'):
                playsound('speech.mp3')
            
    return render(request, 'main/index.html')

