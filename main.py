from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

xor_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
answers = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1))
model.compile(optimizer='sgd', metrics=['acc'], loss='mse')
epochs = 300
performance = []

for i in range(epochs):
    model.fit(x=xor_data, y=answers, batch_size=1, epochs=1, verbose=0)
    loss, acc = model.evaluate(x=xor_data, y=answers, verbose=0)

performance = np.asarray(performance)
plt.plot(performance)
plt.grid()
plt.title("Performance during training")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")

print(model.predict(xor_data))
print(model.summary())
