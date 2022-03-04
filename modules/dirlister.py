import os

def run(**args):
    print('[+] In dirlister moduel')
    files = os.list('.')
    return str(files)
