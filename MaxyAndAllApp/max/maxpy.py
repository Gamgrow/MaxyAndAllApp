import requests
import 
def execute(self):
    response = requests.get(url='https://google.de/search?q=definition%20calcium', proxies=self._proxy)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all("ol", class_="lr_dct_sf_sens")