import requests
from PIL import Image


def get_noice(hexs='', tiles=16, tile_size=1, mode=2):
    url = f'https://php-noise.com/noise.php?hex={hexs}&tiles={tiles}&tileSize={tile_size}&borderWidth=0&mode={mode}'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with Image.open(response.raw) as img:
            img.load()
            return img
    else:
        return False