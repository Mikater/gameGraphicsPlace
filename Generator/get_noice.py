import requests
from PIL import Image


def get_noice(hexs='' | str, tiles=16 | int, tile_size=1 | int, mode=2 | 1 or 2):
    url = f'https://php-noise.com/noise.php?hex={hexs}&tiles={tiles}&tileSize={tile_size}&borderWidth=0&mode={mode}'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with Image.open(response.raw) as img:
            img.load()
            return img
    else:
        return False
