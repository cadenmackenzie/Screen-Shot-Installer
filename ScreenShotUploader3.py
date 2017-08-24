#!/usr/local/bin/python
import os
import datetime
import getpass

'''Take a screen shot and upload it to the cs server'''

def generateName():
    '''Generate a string with the format:
    <username><current date>at<current time>
    '''

    #get the current time
    currenttime = str(datetime.datetime.now())[:-7]
    currenttime = currenttime.replace(" ", "at")
    currenttime = currenttime.replace(":", "_")
    
    #get the current user
    currentuser = str(getpass.getuser())
    
    #declare the name of the screenshot in a string
    scrnShotName = currenttime + currentuser + ".png"
    return scrnShotName

def main():
    '''Take a screenshot, name it, and save it to a file on the CC CompSci server'''
    #Generate a name for the screenshot
    scrnShotName = generateName()
    
    #change directory to desktop
    os.system("cd " + os.path.dirname(os.path.realpath(__file__)))
    
    #save a screen shot of the entire screen after 2 seconds
    #to the directory with name screenshot.png
    os.system("import -window root -delay 200 " + scrnShotName)
    
    #attempt to secure copy to the colorado college
    #computer science server
    os.system('sshpass -p "nsahax" scp ' + scrnShotName + ' appdesign@cs.coloradocollege.edu:public_html/OnTheLine')
    
    #remove the screenshot on the computer's hd
    os.system("rm " + scrnShotName)
    
if __name__ == '__main__':
    main()












