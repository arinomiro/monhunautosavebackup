# Monhun save auto backup

from shutil import copy2
from os.path import getmtime
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

    def checkSaveFile(self):
        self.last_modification = getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000")
        if self.last_modification <= getmtime(self.config["saveDirectory"] + "\\SAVEDATA1000"):
            date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
            copy2(self.config["saveDirectory"] + "\\SAVEDATA1000", self.config["backupDirectory"]+"\\SAVEDATA_" + date)
        

    def startTimer(self):
        timer = Timer(20.0,self.checkSaveFile)
        timer.start()
        



monhun = MonhunSaveAutoBackup("autosaveconftest.json")
monhun.startTimer()
