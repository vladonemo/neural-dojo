from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

xor_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1))
print(model.summary)
