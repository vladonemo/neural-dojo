from datetime import timedelta, datetime
import xlrd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def loadSheet(path):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    arr = []
    counter = 1
    while True:
        try:
            val = xlrd.xldate_as_tuple(sheet.cell_value(counter, 0), book.datemode)
            date = datetime(val[0], val[1], val[2])
            arr.append([date, sheet.cell_value(counter, 2)])
            counter = counter + 1
        except:
            break

    return list(reversed(arr))
