from os import listdir
from os.path import isfile, join


def get_files(path):
    return [join(path, f) for f in listdir(path) if isfile(join(path, f))]
