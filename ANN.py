# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('dataset.csv')
dataset = dataset.replace(255,1)
X = dataset.iloc[:, dataset.columns != 'button'].values
X = np.delete(X,0,1)
X = np.delete(X,3,1)
y = dataset.iloc[:, 5].values

# ------ Data preprocessing ----------

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
onehotencoder = OneHotEncoder()
y = onehotencoder.fit_transform(y.reshape(-1,1)).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train[:,0:3] = sc_X.fit_transform(X_train[:,0:3])
X_test[:,0:3] = sc_X.transform(X_test[:,0:3])

# ------- Build the ANN --------

# import keras library and packages
#import keras
from keras.models import Sequential
from keras.layers import Dense

# Initializing the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
layer_info = Dense(1000 ,input_shape=(5003,),activation='relu',kernel_initializer='uniform')
classifier.add(layer_info)

# Adding second hidden layer
layer_info = Dense(1000,activation='relu', kernel_initializer='uniform')
classifier.add(layer_info)
classifier.add(layer_info)
classifier.add(layer_info)
classifier.add(layer_info)
# Adding output layer
layer_info = Dense(3,activation='softmax', kernel_initializer='uniform')
classifier.add(layer_info)

# Compiling the ANN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fitting the ANN to the training set
classifier.fit(X_train, y_train, batch_size=10, epochs=100)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

b = np.zeros_like(y_pred)
b[np.arange(len(y_pred)), y_pred.argmax(1)] = 1

correct = 0
for i in range(len(b)):
    if (y_test[i] == b[i]).all() :
        correct +=1
print("ACCURACY = "+ str(correct/len(y_pred)))
        
        
