##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################
'''
Created on 11 feb. 2020
@author: omonti
'''

import yaml
import os


class Config():

    def __init__(self):
        self.config = self.loadConfig()

    def loadConfig(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, 'config.yml')
        with open(config_path, 'r') as stream:
            try:
                return yaml.load(stream, yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

    def saveConfig(self):
        with open('config.yml', 'w', encoding='utf8') as configfile:
            yaml.dump(self.config,
                      configfile,
                      default_flow_style=False,
                      allow_unicode=True)

    def getVersion(self):
        return self.config['version']

    def getPathToProjectsFolder(self):
        return self.config["paths"]["projects"]

    def getPathData(self):
        return self.config["paths"]["data"]

    def setPathData(self, path):
        if (path is not None and path != ''):
            self.config["paths"]["data"] = path
            self.saveConfig()

    def getPathHistories(self):
        hist = self.config["paths"]["histories"]
        newHist = []
        if hist:
            for h in hist:
                if os.path.exists(h):
                    newHist.append(h)
        self.setPathHistories(newHist)
        return newHist

    def setPathHistories(self, hist):
        self.config["paths"]["histories"] = hist
        self.saveConfig()

    def getPathProjectsFile(self):
        folder = self.getPathToProjectsFolder()
        return os.path.join(folder, 'projects.json')

    def getPathLibraries(self):
        return self.config['packages']
    
    def getPathDiagrams(self):
        diag = self.config["paths"]["diagrams"]
        return list(diag)
        
    def setPathDiagrams(self, diag):
        self.config["paths"]["diagrams"] = diag
        self.saveConfig()
