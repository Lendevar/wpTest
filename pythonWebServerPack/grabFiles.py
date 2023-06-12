import shutil
import os
import time

fromDirectory = '../laravel/TestDirectory/'
toDirectory = 'pythonWebServer/'

filesInFromDirectory = []

def printTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)



def copyAllFilesFromDirectory(withDeletion):
    print("===================")
    printTime()
    print("Origin directory content: " + str(filesInFromDirectory))
    for fileToCopy in filesInFromDirectory:
        with open(toDirectory+fileToCopy, 'w') as f:
            f.write('')

        shutil.copy(fromDirectory+fileToCopy, toDirectory+fileToCopy)
        print("File "+fromDirectory+fileToCopy+" copied to "+toDirectory+fileToCopy)

        if withDeletion:
            if os.path.exists(fromDirectory+fileToCopy):
                os.remove(fromDirectory+fileToCopy)
                print("With Deletion in Origin!")
            else:
                print("The file does not exist")
        else:
            print("Without Deletionазаза")

while True:
    filesInFromDirectory = os.listdir(fromDirectory)
    copyAllFilesFromDirectory(True)
    time.sleep(10)
