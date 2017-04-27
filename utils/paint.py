"""parse data"""
from parseData import ParseData
import numpy as np
import string


class PaintData(object):
    def __init__(self, filePath):
        data = ParseData(filePath)
        self.__timeZoneData = data.get_time_zone_data()

    def getTdata(self):
        return self.__timeZoneData

    def getHdata(self):
        hData = {}
        interval = self.getHInterval(self.__timeZoneData['x'])
        hData['x'] = [interval * i for i in range(len(self.__timeZoneData['x']))]
        hData['y'] = np.fft.fft(np.array(self.__timeZoneData['y']))
        hData['speaks'] = self.findSpeaks(hData['y'])
        return hData

    def getHInterval(self, timeZoneData):
        return round(1 / string.atof(timeZoneData[-1]), 2)

    def findSpeaks(self, listData):
        posListData = [abs(i) for i in listData]
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



