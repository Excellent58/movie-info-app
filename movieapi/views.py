from django.shortcuts import render

import requests

def Home(request):
    if request.method == 'POST':
        title = request.POST['title']

        movie_data = get_movie_info(title).json() #items d, q, v
        title = movie_data['d'][1]['l']
        year = movie_data['d'][1]['y']
        stars = movie_data['d'][0]['s']
        imageUrl = movie_data['d'][1]['i']['imageUrl']
        movie_id = movie_data['d'][1]['id']
        
        movie_url = f"https://www.imdb.com/title/{movie_id}"

        context = {
            'movie_data': {
                'title': title,
                'imageUrl': imageUrl,
                'year': year,
                'movie_url': movie_url,
                'stars': stars
            },
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')


def get_movie_info(title):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q":title}
    headers = {
        "X-RapidAPI-Key": "dab64a933emshd4feed0a110bc98p1fa4f0jsncfc1e252bd18",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response