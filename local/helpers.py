from constants import DFD_PATH, TXT_PATH
from pathlib import Path
import os
import shutil


def convert_file_to_txt():
    
    carpeta = Path(DFD_PATH)
    
    for f in (carpeta.iterdir()):
        if f.suffix == '.dfd':
            new_extension = f.with_suffix('.txt')
            f.rename(new_extension)
            shutil.move(new_extension, TXT_PATH)

def convert_file_to_dfd():
    
    carpeta = Path(TXT_PATH)
    
    for f in (carpeta.iterdir()):
        if f.suffix == '.txt':
            new_extension = f.with_suffix('.dfd')
            f.rename(new_extension)
        shutil.move( new_extension, DFD_PATH)

# def convert_one_file_to_dfd(f):