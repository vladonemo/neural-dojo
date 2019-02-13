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


def fillGap(arr):
        length = len(arr)
        x = []
        y = []
        all = []
        for i in range(length):
            if i != 0:
                delta = arr[i][0] - arr[i - 1][0]
                diff = delta.days
                if diff > 1:
                    date = arr[i - 1][0]
                    diff = diff - 1
                    for j in range(diff):
                        date += timedelta(days=1)
                        x.append(date)
                        y.append(arr[i - 1][1])
                        all.append([date, arr[i - 1][1]])
            x.append(arr[i][0])
            y.append(arr[i][1])
            all.append([arr[i][0], arr[i][1]])
        return [x, y, all]


data = loadSheet("fund.xls")
