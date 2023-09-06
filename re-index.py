import os
from pathlib import Path
import json

p = Path("/home/charlesohanlon/Development/Datasets/ImageNet/Data/train")
sub_dirs = os.listdir(p)
sub_dirs.sort()

with open("id2class.json", "r") as file:
    contents = json.load(file)

for i, dir in enumerate(sub_dirs):
    contents[dir][1] = i

with open("id2class.json", "w") as file:
    json.dump(contents, file)

