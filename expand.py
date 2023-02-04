import json
import shutil
from os import listdir, makedirs
from os.path import isfile, join, exists

import tqdm

"""
    Questo modulo organizza le immagini in cartelle
    in base alla loro etichetta
"""

PATH = "."

IMG_PATH = PATH + "/images_300"

onlyfiles = [f for f in listdir(IMG_PATH) if isfile(join(IMG_PATH, f))]
onlyfiles.sort()

data = {}
try:
    with open(PATH + '/data.json') as json_file:
        data = json.load(json_file)
except:
    pass

if not exists(join(PATH, "Pollen")):
    makedirs(join(PATH, "Pollen"))
if not exists(join(PATH, "None")):
    makedirs(join(PATH, "None"))
if not exists(join(PATH, "Varroa")):
    makedirs(join(PATH, "Varroa"))
if not exists(join(PATH, "Cooling")):
    makedirs(join(PATH, "Cooling"))
if not exists(join(PATH, "Wasps")):
    makedirs(join(PATH, "Wasps"))

for item in tqdm.tqdm(data):

    path = "images_300/" + item
    e = data[item]
    a = e["varroa"] or e["pollen"] or e["cooling"] or e["wasps"]

    if e["varroa"]:
        shutil.copy(path, "Varroa")
    if e["pollen"]:
        shutil.copy(path, "Pollen")
    if e["wasps"]:
        shutil.copy(path, "Wasps")
    if e["cooling"]:
        shutil.copy(path, "Cooling")

    if not a:
        shutil.copy(path, "None")
