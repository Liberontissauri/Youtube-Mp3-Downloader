import os

def create_folder_structure():
    if not os.path.isdir("./tmp"):
        os.mkdir("./tmp")

    if not os.path.isdir("./mp3"):
        os.mkdir("./mp3")

def deletetmpfiles():
    for file in os.listdir("./tmp"):
        os.remove("".join(("./tmp/",file)))