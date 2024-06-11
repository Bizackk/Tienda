from django.shortcuts import render, redirect
import requests

def home(request):
    url = "https://api.rawg.io/api/games"
    params = {
        'key': '4f1c315daca547a5b3a2291a54383c6b',
        'page_size': 20
    }
    response = requests.get(url, params=params)
    juegos = response.json().get('results', [])

    if request.method == "POST":
        selected_game_id = request.POST.get('game')
        return redirect('detalles', game_id=selected_game_id)

    return render(request, 'home.html', {'juegos': juegos})

def detalle_juego(request, game_id):
    url = f"https://api.rawg.io/api/games/{game_id}"
    params = {
        'key': '4f1c315daca547a5b3a2291a54383c6b'
    }
    response = requests.get(url, params=params)
    juego = response.json()

    return render(request, 'detalles.html', {'juego': juego})
