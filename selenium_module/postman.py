import requests
import json
from urllib.request import urlopen

url = 'https://api.nasa.gov/planetary/apod?api_key=UsaPEV8c4pUkHvs2dzOPjQAfhoiKHec9fx4Chs38'


response = requests.get(url)
print(type(response))
print(response)   
print(response.status_code) 
print(response.json)
print(response.text) 

if response.status_code == 200:
    data = response.json()
    print(response.json())
    print(data['title'])
    print(data['date'])
    print(data['url'])
elif response.status_code == 429:
    print(response.json())
else:
    print('fail')

# <Response [200]>
# 200
# <bound method Response.json of <Response [200]>>
# {"copyright":"\nCarlos Taylor\n","date":"2024-06-19","explanation":"Do dragons fight on the altar of the sky?  Although it might appear that way, these dragons are illusions made of thin gas and dust. The emission nebula NGC 6188, home to the glowing clouds, is found about 4,000 light years away near the edge of a large molecular cloud, unseen at visible wavelengths, in the southern constellation Ara (the Altar). Massive, young stars of the embedded Ara 
# OB1 association were formed in that region only a few million years ago, sculpting the dark shapes and powering the nebular glow with stellar winds and intense ultraviolet radiation. The recent star formation itself was likely triggered by winds and supernova explosions from previous generations of massive stars, that swept up and compressed the molecular gas. This impressively detailed image spans over 2 degrees (four full Moons), corresponding to over 
# 150 light years at the estimated distance of NGC 6188.","hdurl":"https://apod.nasa.gov/apod/image/2406/AraDragons_Taylor_4728.jpg","media_type":"image","service_version":"v1","title":"NGC 6188: Dragons of Ara","url":"https://apod.nasa.gov/apod/image/2406/AraDragons_Taylor_960.jpg"}

# {'copyright': '\nCarlos Taylor\n', 'date': '2024-06-19', 'explanation': 'Do dragons fight on the altar of the sky?  Although it might appear that way, these dragons are illusions made of thin gas and dust. The emission nebula NGC 6188, home to the glowing clouds, is found about 4,000 light years away near the edge of a large molecular cloud, unseen at visible wavelengths, in the southern constellation Ara (the Altar). Massive, young stars of the embedded Ara OB1 association were formed in that region only a few million years ago, sculpting the dark shapes and powering the nebular glow with stellar winds and intense ultraviolet radiation. The recent star formation itself was likely triggered by winds and supernova explosions from previous generations of massive stars, that swept up and compressed the molecular gas. This impressively detailed image spans over 2 degrees (four full Moons), corresponding to 
# over 150 light years at the estimated distance of NGC 6188.', 'hdurl': 'https://apod.nasa.gov/apod/image/2406/AraDragons_Taylor_4728.jpg', 'media_type': 'image', 'service_version': 'v1', 'title': 'NGC 6188: Dragons of Ara', 'url': 'https://apod.nasa.gov/apod/image/2406/AraDragons_Taylor_960.jpg'}
# NGC 6188: Dragons of Ara
# 2024-06-19
# https://apod.nasa.gov/apod/image/2406/AraDragons_Taylor_960.jpg


# или можно получить такой ответ после превышения лимита запросов

# <class 'requests.models.Response'>
# <Response [429]>
# 429
# <bound method Response.json of <Response [429]>>
# {
#   "error": {
#     "code": "OVER_RATE_LIMIT",
#     "message": "You have exceeded your rate limit. Try again later or contact us at https://api.nasa.gov:443/contact/ for assistance"
#   }
# }
# fail