import numpy as np
import os
import random
from shutil import copyfile

image_path = './testing/'
dest = './test/'

for cat in os.listdir(image_path):
    im_path  = os.path.join(image_path, cat)
    new_path = os.path.join(dest, cat)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    list = os.listdir(im_path)
    shortlisted = random.choices(list, k=10)
    for f in shortlisted:
        full_path = os.path.join(im_path, f)
        full_path_new = os.path.join(new_path, f)
        copyfile(full_path, full_path_new)
        print(full_path, ' -> ', full_path_new)
