"""parse data"""
from parseData import ParseData
import numpy as np
import scipy as sp


class PaintData(object):
    def __init__(self, filePath):
        data = ParseData(filePath)
        self.__timeZoneData = data.get_time_zone_data()

    def getTdata(self):
        return self.__timeZoneData

    def getHdata(self):
        hData = {}
        hData['x'] = self.__timeZoneData['x']
        hData['y'] = sp.fft(np.array(self.__timeZoneData['y']))
        return hData
