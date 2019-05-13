import shutil
import os

def move(destination, depth=None):
    if not depth:
        depth = []
    for file_or_dir in os.listdir(os.path.join([destination] + depth, os.sep)):
        if os.path.isfile(file_or_dir):
            shutil.move(file_or_dir, destination)
        else:
            move(destination, os.path.join(depth + [file_or_dir], os.sep))

base = './mnist_test_output'
for category in os.listdir(base):
    dest = os.path.join(base,category)
    # dest = base
    path = os.path.join(dest, 'fixations')
    for fil in os.listdir(path):
        currentFile = os.path.join(path, fil) + '/fixationList.mat'
        destination = os.path.join(dest, fil) + '.mat'
        print(currentFile, destination)
        shutil.move(currentFile, destination)

    shutil.rmtree(path)
    