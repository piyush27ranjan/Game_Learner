import pandas as pd

column =['b_x','b_y','p_x','time']
for i in range(1,5001):
    column.append(i)
    
coordinate = pd.read_csv('dataset_coordinates.csv',names=column, skiprows=1)
keylogger = pd.read_csv('dataset_keylogger.csv',header=None, skiprows=1)
button = []
time = coordinate.iloc[:,3]

k=0

for t in range(len(time)):
    print(t)
    for j in range(k,len(keylogger)):
        if keylogger[2][j] > time[t] > keylogger[1][j]:
            button.append(keylogger[0][j])
            k=j
            break
        elif keylogger[2][j] > time[t]:
            button.append("None")
            k=j
            break

coordinate.insert(4,"button",button)

coordinate.to_csv("dataset.csv")
    
