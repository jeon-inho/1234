import glob
import shutil
import os

dir = ("c:/2")

for name in glob.glob("c:/1/*.dna"):
    fileNm  = os.path.basename(name)
    fileNm  = (os.path.splitext(os.path.basename(name))[0]).strip()
    if len(fileNm) > 11:  continue 
    
    FileExt = (os.path.splitext(name)[1]).strip()
    #shutil.move(name, dir)
    print(name)

