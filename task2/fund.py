from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from datetime import timedelta, datetime
import xlrd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

window = 5


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


def createDataset(scaled, window_size):
    actual = 0
    target = window_size
    length = scaled.shape[0]
    x = []
    y = []

    while target < length:
        x.append(scaled[actual: actual + window_size].tolist())
        y.append(scaled[target])
        target = target + 1
        actual = actual + 1
    x = np.asarray(x)
    x = x.reshape(x.shape[0], window_size)
    y = np.asarray(y)
    return x, y


data = loadSheet("fund.xls")
x, y, everything = fillGap(data)
y = np.asarray(y)

plt.plot(y)
plt.xlabel("Days")
plt.ylabel("Fund price [EUR]")
plt.title("Funt value over time")
plt.show()

y = y.reshape(-1, 1)
scaler = MinMaxScaler(copy=True, feature_range=(0, 1))
scaler.fit(y)
x, y = createDataset(scaler.transform(y), window)
train = 0.8
length = x.shape[0]
train_length = int(train * length)
x_train = x[0: train_length, :]
y_train = y[0: train_length]
x_test = x[train_length: length, :]
y_test = y[train_length: length]

model = Sequential()
model.add(Dense(20, input_shape=(window,), activation="sigmoid"))
model.add(Dense(1))
model.compile(optimizer="sgd", loss="mse", metrics=["acc"])
model.fit(x_train, y_train, epochs=1000, batch_size=25, verbose=0)
model.evaluate(x_train, y_train)

predicted = model.predict(x_test)
plt.plot(y_test, "green", predicted, "red")
plt.show()
