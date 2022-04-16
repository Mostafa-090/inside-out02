from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
model = load_model("model.h5")


def EmoPredictor(signals):
    predicted=np.array(list(map(lambda x: np.argmax(x), new_model.predict(signals))))
    if predicted == [0]:
        return "Sad"
    elif predicted == [1]:
        return "Natural"
    else:
        return "Happy"


def emopredict(data_test):
    y = data_test.pop('label')
    X = data_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9)
    X_train = np.array(X_train).reshape((X_train.shape[0],X_train.shape[1],1))
    X_test = np.array(X_test).reshape((X_test.shape[0],X_test.shape[1],1))
    y_train = pd.get_dummies(y_train)
    y_test = pd.get_dummies(y_test)
    
    predicted=np.array(list(map(lambda x: np.argmax(x), model.predict(X_test))))
    if predicted == [0]:
        return "\N{crying face}  Sad"
    elif predicted == [1]:
        return "\N{neutral face}  Natural"
    else:
        return "\N{grinning face with smiling eyes}  Happy"