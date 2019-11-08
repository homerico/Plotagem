import os

def find(name, path, type='file'):
    for root, dirs, files in os.walk(path):
        if type=='file':
            if name in files:
                return os.path.join(root, name)
        elif type=='dir':
            if name in dirs:
                return os.path.join(root, name)

    raise FileNotFoundError