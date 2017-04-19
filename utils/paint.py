"""parse data"""
from parseData import ParseData
import numpy as np


class PaintData(object):
    def __init__(self, filePath):
        data = ParseData(filePath)
        self.__timeZoneData = data.get_time_zone_data()

    def getTdata(self):
        return self.__timeZoneData

    def getHdata(self):
        hData = {}
        hData['x'] = self.__timeZoneData['x']
        hData['y'] = np.fft.fft(np.array(self.__timeZoneData['y']))
        self.findSpeaks(hData['y'])
        return hData

    def findSpeaks(self, listData):
        posListData = [ abs(i) for i in listData ]
        maxValue = max(posListData)
        speakIndexList = []
        resList = []
        for i in range(len(posListData) - 1):
            if posListData[i - 1] < posListData[i] > posListData[i + 1]:
                speakIndexList.append(i)

        for i in speakIndexList:
            if posListData[i] * 1.0 / maxValue > 0.05:
                resList.append(i)

        return resList



