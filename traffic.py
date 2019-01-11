import pandas as pd

data = [12, 12, 30, 12, 11, 5, 7, 10, 13]
for index in range(len(data)):
    if data[index] == 30:
        break
    elif data[index] >= 1 and data[index] < 10:
        print('Green light')
       
    elif data[index] < 20:
        print('Yellowww light')
    elif data[index] < 30:
        print("Red light")

    else:
        data[index] = 0
    
data2 = pd.read_csv("/home/bid/Desktop/noquote.csv", sep=",", header=None)
print(data2)
print(data2)
