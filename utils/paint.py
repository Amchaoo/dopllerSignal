"""parse data"""
from parseData import ParseData
import numpy as np
import string
from scipy import signal as sg
from scipy import fftpack as fp
from utils.xcorr import CORRELATION
import matplotlib.pyplot as plt


class PaintData(object):
    def __init__(self, filePath):
        data = ParseData(filePath)
        self.__timeZoneData = data.get_time_zone_data()
        self.__hZoneData = self.calculateFFT(self.__timeZoneData)
        self.__xcorrTimeData = self.calXcorrTData(self.__timeZoneData)
        self.__xcorrHZoneData = self.calculateFFT(self.__xcorrTimeData)
        self.__HZoneDataWithWindow = self.calFFTWithWidow(self.__timeZoneData)
        self.__xcorrHZoneDataWithWindow = self.calFFTWithWidow(self.__xcorrTimeData)

        """
        test start
        """
        # f = open('a.html', 'wb')
        # f.writelines(str(self.__timeZoneData['y']))
        # self.paintH(data.get_hz_zone_data())
        """
        test end
        """

    def calculateFFT(self, timeZoneData):
        hData = {
            'x': [],
            'y': [],
            'speaks': []
        }
        size = len(timeZoneData['y'])
        hData['x'] = fp.fftfreq(size, timeZoneData['x'][-1]/size)[0:size/2]
        hData['x'] = [round(i, 2) for i in hData['x']]
        hData['y'] = abs(fp.fft(timeZoneData['y']))[0:size/2]
        hData['speaks'] = self.findSpeaks(hData['y'])

        return hData

    def calFFTWithWidow(self, timeZoneData):
        hData = {
            'x': [],
            'y': [],
            'speaks': []
        }
        fs = round(1 / string.atof(timeZoneData['x'][-1]), 2) * len(timeZoneData['x'])
        print fs

        hData['x'], hData['y'] = sg.welch(
            timeZoneData['y'],
            fs=fs,
            window=sg.get_window('hamming', len(timeZoneData['x'])))
        hData['speaks'] = self.findSpeaks(hData['y'])

        return hData

    def calXcorrTData(self, xcorrTimeZoneData):
        xcorrTData = {
            'x': xcorrTimeZoneData['x'],
            'y': []
        }
        xcorrTData['y'] = CORRELATION(xcorrTimeZoneData['y'])
        xcorrTData['y'] = CORRELATION(xcorrTData['y'])
        xcorrTData['y'] = CORRELATION(xcorrTData['y'])
        return xcorrTData

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
            if posListData[i] * 1.0 / maxValue > 0.08:
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

    def getHZoneDataWithWindow(self):
        return self.__HZoneDataWithWindow

    def getXcorrHZoneDataWithWindow(self):
        return self.__xcorrHZoneDataWithWindow

    # def paintH(self, data):
    #     plt.figure()
    #     plt.subplot(111)
    #     plt.plot(data['x'], abs(np.array(data['y'])))
    #     for index in self.findSpeaks(data['y']):
    #         plt.annotate(
    #             data['x'][index],
    #             xy=(data['x'][index], data['y'][index]),
    #             xytext=(1, 30),
    #             textcoords='offset points',
    #             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
    #     plt.show()