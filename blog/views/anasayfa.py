from django.shortcuts import render


def anasayfa(request):
    context = {
        'isim': 'Soner Arslan'
    }
    return render(request, 'pages/anasayfa.html', context=context)
