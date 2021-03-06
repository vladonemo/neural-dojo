from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras.callbacks import TensorBoard
from time import time

xor_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
answers = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1))
model.compile(optimizer='sgd', metrics=['acc'], loss='mse')
epochs = 300
performance = []
tensorboard = TensorBoard(log_dir="logs/{}".format(time()), write_graph=True)

model.fit(x=xor_data, y=answers, batch_size=1, epochs=epochs, verbose=0, callbacks=[tensorboard])
loss, acc = model.evaluate(x=xor_data, y=answers, verbose=0)
performance.append(acc)

performance = np.asarray(performance)
plt.plot(performance)
plt.grid()
plt.title("Performance during training")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.show()

print(model.predict(xor_data))
print(model.summary())
