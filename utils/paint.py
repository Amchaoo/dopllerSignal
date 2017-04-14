"""parse data"""
from parseData import ParseData
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    INS = ParseData('./../data/ADRS0019.CSV')
    TIME_ZONE_DATA = INS.get_time_zone_data()
    HZ_ZONE_DATA = INS.get_hz_zone_data()

    res = np.fft.fft(np.array(TIME_ZONE_DATA['y']))

    print res
    print len(TIME_ZONE_DATA['y'])
    plt.subplot(211)
    plt.plot(TIME_ZONE_DATA['x'], res)

    plt.subplot(212)
    plt.plot(HZ_ZONE_DATA['x'], HZ_ZONE_DATA['y'])

    plt.show()