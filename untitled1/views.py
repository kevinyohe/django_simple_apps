from django.http import HttpResponse
from django.shortcuts import render


def hello(request):

    return render(request, 'home.html')


def translate(request):
    text1 = request.GET['originaltext'].lower()
    text1.split()
    translation = ''

    for word in text1.split():
        if word[0] in ['a','e','i','o','u']:
            #vowel
            translation += word
            translation += 'yay '
        else:
            #consonant
            translation += word[1:]
            translation += word[0]
            translation += 'ay '
    if translation == '':
        translation = 'no text entered!'

    #return HttpResponse(translation)
    return render(request, 'translate.html', {'original': text1, 'translation': translation})
