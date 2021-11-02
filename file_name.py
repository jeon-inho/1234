import os

name = strip(".{:5}.mp3")
print (name)
for filename in os.listdir("."):
    if filename.startswith(name):
        os.rename(filename, name)
