# Monhun save auto backup

from shutil import copy2
from os.path import getmtime, getctime
from os import listdir, remove
from threading import Timer
from datetime import datetime
import json

class MonhunSaveAutoBackup():
    """Script that automatically backs up save files after they are written"""
    

    def __init__(self, conf_path="autosaveconf.json"):
        with open(conf_path) as json_file:
            data = json.load(json_file)
        self.config = data
        self.last_modification = None
        json_file.close()
        return None
    

    def checkFileLimit(self):
        list_of_files = listdir(self.config["backupDirectory"]);
        oldest_file = "";
        full_path = [self.config["backupDirectory"] + "/{0}".format(x) for x in list_of_files]
        # Check the maximum number of backups is being honored.
        # If it isn't, remove the oldest entry.
        if len(list_of_files) > self.config["maxNumberOfBackups"]:
            print "Backup limit has been reached. Removing oldest entry..."
            oldest_file = min(full_path, key=getctime)
            remove(oldest_file)
            
        elif len(list_of_files) == self.config["maxNumberOfBackups"]:
            print "Backup limit reached. The oldest file will be removed in the next check."
            

    def checkSaveFile(self):
        self.last_modification = getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000") if self.last_modification is None else self.last_modification
        print "Checking savefile..."
        
        if self.last_modification < getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000"):
            print "Savefile has been modified, backing up changes..."
            self.checkFileLimit()
            # Generate the backup's file name and save it to the specified location.
            date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            copy2(self.config["saveDirectory"] + "\\SAVEDATA1000", self.config["backupDirectory"]+"\\SAVEDATA1000_" + date)
            print "Backup saved in {0}".format(self.config["backupDirectory"]+"\\SAVEDATA1000_" + date)
            
        self.last_modification = getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000")
        self.startTimer()
        

    def startTimer(self):
        self.timer = Timer(20.0,self.checkSaveFile)
        self.timer.start()
        



monhun = MonhunSaveAutoBackup()
monhun.startTimer()
print "Script started"
