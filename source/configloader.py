# -*- coding: utf-8 -*-
"""
@author: EdibleEd
"""
import configparser, os

FILENAME = 'config.cfg'
# Config file is in root of the project
filepath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)), FILENAME)

class ConfigLoader:

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read(filepath)

    def getResolution(self):
        return(self.parser.get('Graphics Settings','resolutionx'), self.parser.get('Graphics Settings','resolutiony'))

# Testing
if __name__ == "__main__":
    loader = ConfigLoader()
    print(loader.getResolution())
