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
        json_file.close()
        return None
    

    def checkFileLimit(self):
        list_of_files = listdir(self.config["backupDirectory"]);
        oldest_file = "";
        full_path = [self.config["backupDirectory"] + "/{0}".format(x) for x in list_of_files]
        
        if len(list_of_files) >= self.config["maxNumberOfBackups"]:
            oldest_file = min(full_path, key=getctime)
            remove(oldest_file)
            

    def checkSaveFile(self):
        self.last_modification = getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000")
        if self.last_modification <= getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000"):
            self.checkFileLimit()
            date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
            copy2(self.config["saveDirectory"] + "\\SAVEDATA1000", self.config["backupDirectory"]+"\\SAVEDATA_" + date)
        self.startTimer()
        

    def startTimer(self):
        self.timer = Timer(20.0,self.checkSaveFile)
        self.timer.start()
        



monhun = MonhunSaveAutoBackup("autosaveconftest.json")
monhun.startTimer()
