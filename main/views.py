from django.shortcuts import render
from googletrans import Translator

def index(request):
    if request.method == 'POST':
        lang = request.POST.get('lang')
        lang1, lang2 = lang.split(',')
        txt = request.POST.get('txt')

        translator = Translator()
        tr = translator.translate(txt, dest=lang1)

        return render(request, 'main/index.html', {'result': tr.text})
    return render(request, 'main/index.html')
