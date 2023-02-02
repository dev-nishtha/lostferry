from django.shortcuts import render
from .models import Artist
import requests
# Create your views here.


def home(request):
    return render(request, 'search_music.html')


def search_result(request):
    all_results = {}
    if 'query' in request.GET:
        query = request.GET['query']
        url = 'https://itunes.apple.com/search?term=%s&media=music&entity=album' % query
        response = requests.get(url)
        data = response.json()
        artists = data['results']

        for i in artists:
            artist_data = Artist(
                artist=i['artistName'],
                album=i['collectionName'],
                album_url=i['collectionViewUrl'],
                album_cover=i['artworkUrl100']
            )
            artist_data.save()
            all_results = Artist.objects.filter(artist__contains=query)

        return render(request, 'search_result.html', {'query': query, 'all_results': all_results})
