"""parse data"""
from parseData import ParseData
import matplotlib.pyplot as plt

if __name__ == '__main__':
    INS = ParseData('./../data/ADRS0005.CSV')
    TIME_ZONE_DATA = INS.get_time_zone_data()
    HZ_ZONE_DATA = INS.get_hz_zone_data()

    plt.subplot(211)
    plt.plot(TIME_ZONE_DATA['x'], TIME_ZONE_DATA['y'])

    plt.subplot(212)
    plt.plot(HZ_ZONE_DATA['x'], HZ_ZONE_DATA['y'])

    plt.show()
