#verifico que en la carpetea cylinder/test existan solamente archivos .jpg y .txt
import os
import sys
import re

def check_files():
    files = os.listdir('cylinder/train')
    for file in files:
        if not re.match(r'.*\.jpg|.*\.txt', file):
            print('Error: en la carpeta cylinder/test existen archivos que no son .jpg o .txt')
            sys.exit(1)
    print('Todos los archivos en cylinder/test son .jpg o .txt')