"""parse data"""
from parseData import ParseData
import numpy as np
import string
from scipy import fftpack as fp


class PaintData(object):
    def __init__(self, filePath):
        data = ParseData(filePath)
        self.__timeZoneData = data.get_time_zone_data()
        self.__hZoneData = self.calculateFFT(self.__timeZoneData)
        self.__xcorrTimeData = self.calXcorrTData(self.__timeZoneData)
        self.__xcorrHZoneData = self.calculateFFT(self.__xcorrTimeData)

    def calculateFFT(self, timeZoneData):
        hData = {
            'x': [],
            'y': [],
            'speaks': []
        }

        interval = self.getHInterval(timeZoneData['x'])
        hData['x'] = [interval * i for i in range(len(timeZoneData['x']))]
        hData['y'] = fp.fft(np.array(timeZoneData['y']))
        hData['y'] = [abs(i) for i in hData['y']]
        hData['speaks'] = self.findSpeaks(hData['y'])

        return hData

    def calXcorrTData(self, xcorrTimeZoneData):
        xcorrTData = {
            'x': xcorrTimeZoneData['x'],
            'y': []
        }
        xcorrTData['y'] = xcorr(np.array(
            xcorrTimeZoneData['y']),
            np.array(xcorrTimeZoneData['y']), 'unbiased')
        return xcorrTData

    def getHInterval(self, timeZoneData):
        return round(1 / string.atof(timeZoneData[-1]), 2)

    def findSpeaks(self, listData):
        posListData = [abs(i) for i in listData]
        maxValue = max(posListData)
        speakIndexList = []
        resList = []
        print maxValue
        for i in range(len(posListData) - 1):
            if posListData[i - 1] < posListData[i] > posListData[i + 1]:
                speakIndexList.append(i)

        for i in speakIndexList:
            if posListData[i] * 1.0 / maxValue > 0.2:
                resList.append(i)

        return resList

    def getTimeZoneData(self):
        return self.__timeZoneData

    def getHZoneData(self):
        return self.__hZoneData

    def getXcorrTimeZoneData(self):
        return self.__xcorrTimeData

    def getXcorrHZoneData(self):
        return self.__xcorrHZoneData


def xcorr(x, y, scale='none'):
    size = x.size

    corr = np.correlate(x, y, mode='full')  # scale = 'none'
    lags = np.arange(-(x.size - 1), x.size)

    if scale == 'biased':
        corr = corr / x.size
    elif scale == 'unbiased':
        corr /= (x.size - abs(lags))
    elif scale == 'coeff':
        corr /= np.sqrt(np.dot(x, x) * np.dot(y, y))
    return corr[size - 1:corr.size]
   # hData['x'], hData['y'] = sg.welch(self.__timeZoneData['y'], fs = 1024, window=sg.get_window('hamming',256))