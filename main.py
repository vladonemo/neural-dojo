from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np

xor_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
answers = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1))
model.compile(optimizer='sgd', metrics=['acc'], loss='mse')
model.fit(x=xor_data, y=answers, batch_size=1, epochs=10000, verbose=0)
print(model.predict(xor_data))
print(model.summary)
