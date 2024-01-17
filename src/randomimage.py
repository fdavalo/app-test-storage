import requests
import shutil
import urllib.request
import time
import random
import datetime
import os

token = urllib.request.urlopen("http://10.6.82.67:81/nijaapitoken.txt").read().strip()
category = 'nature'
api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
while True:
    response = requests.get(api_url, headers={'X-Api-Key': token, 'Accept': 'image/jpg'}, stream=True)
    if response.status_code == requests.codes.ok:
        fn = datetime.datetime.now().strftime('%m%d%Y-%H%M%S')
        with open(fn+'.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error:", response.status_code, response.text)
    time.sleep(random.randrange(10))
    if os.path.isfile(os.environ['FS']+"/stop"): break 
