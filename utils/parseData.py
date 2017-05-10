"""this moudle read csv file"""
import csv
import string


class ParseData(object):

    __row_data = ''

    def __init__(self, file_name):
        self.__file = open(file_name)
        self.__row_data = self.__get_row_data()

    def __get_row_data(self):
        return csv.reader(self.__file)

    def __slice_data(self, start_flag, end_flag):
        flag = False
        result = {
            'x': [],
            'y': []
        }
        for row in self.__row_data:
            if row == end_flag:
                flag = False

            if flag:
                if row[0] != 'OA':
                    result['x'].append(string.atof(row[0]))
                    result['y'].append(float(row[1]))

            if row == start_flag:
                flag = True
        self.__file.seek(0)
        return result

    def get_time_zone_data(self):
        """get time zone data"""
        return self.__slice_data(['TIME(s)', 'TIMEa(EU)'], [])

    def get_hz_zone_data(self):
        """get hz zone data"""
        return self.__slice_data(['FREQ(Hz)', 'SPECa(EU)'], ['OAW', '-'])
