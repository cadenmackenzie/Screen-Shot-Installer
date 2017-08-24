import os


commandList = ['ssh -t remotehost "sudo" apt-get install imagemagick',
               "sudo apt-get install sshpass",
               "sudo pip install pyinstaller",
               "pyinstaller --onefile --windowed ScreenShotUploader.py",
               "sudo apt-get install xbindkeys",
               "sudo apt-get install xbindkeys-config",
               ]


os.system(commandList[0])
