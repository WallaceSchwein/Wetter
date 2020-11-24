import requests
from bs4 import BeautifulSoup
from .CraweledData import CraweledData

class DataGetter():
    def get(self):
        r = requests.get("https://www.wetter.com/wetter_aktuell/wettervorhersage/16_tagesvorhersage/deutschland/berlin/DE0001020.html")
        k = BeautifulSoup(r.text, "html.parser")

        for item in k.select(".weather-grid-item"):
            tag_raw = item.select_one(".text--orange") or item.select_one(".text--white")
            tag = tag_raw.text
            max = item.select_one(".temp-max").text
            min = item.select_one(".temp-min").text[3:]
            regen_l = item.select_one(".weather-state").text.split()
            regen = " ".join(regen_l)

            yield CraweledData(tag, max, min, regen)