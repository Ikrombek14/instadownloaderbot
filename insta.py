import requests
import json
def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "2a7db66b70msh6013d6fe4052286p1f5a20jsn6639ee5f411c",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict={}
        if rest['Type'] == 'Post-Image':
            dict['type']='image'
            dict['type']=rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Carusel':
            dict['type'] = 'carusel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'

