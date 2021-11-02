import glob
import shutil
import os

dir = 'c:/2'

for name in glob.glob("c:/1/*[0:14].dna"):
    print(name)
    #shutil.move(name, dir)

