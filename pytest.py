import mysql.connector
import pandas as pd
import numpy as numpy
import pickle
from sklearn.ensemble import IsolationForest



# print(myresult)



data = pd.read_csv("sub_data_2.csv", index_col = None)
print(data)
data = data.drop(columns=["dtlog"], axis=1)
print (data.head())

data['0-3']=0
data['4-7']=0
data['8-11']=0
data['12-15']=0
data['16-19']=0
data['20-23']=0
print(data.head())

nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour00"][i] + data["Hour01"][i] + data["Hour02"][i] + data["Hour03"][i]
    data.loc[i,"0-3"] = sum_hours
# index = 0
# for i in data["0-3"]:
#     if i != 0:
#         print(str(index) + " : " + str(i))
#     index = index + 1
# data.iloc[:, 40:]

nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour04"][i] + data["Hour05"][i] + data["Hour06"][i] + data["Hour07"][i]
    data.loc[i, "4-7"] = sum_hours


nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour08"][i] + data["Hour09"][i] + data["Hour10"][i] + data["Hour11"][i]
    data.loc[i, "8-11"] = sum_hours


nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour12"][i] + data["Hour13"][i] + data["Hour14"][i] + data["Hour15"][i]
    data.loc[i, "12-15"] = sum_hours


nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour16"][i] + data["Hour17"][i] + data["Hour18"][i] + data["Hour19"][i]
    data.loc[i, "16-19"] = sum_hoursindex = 0


nrows = len(data.iloc[:,0])
for i in range(nrows):
    sum_hours = data["Hour20"][i] + data["Hour21"][i] + data["Hour22"][i] + data["Hour23"][i]
    data.loc[i, "20-23"] = sum_hours

print(data)

data['North America']=0
data['South America']=0
data['South Asia']=0
data['East Asia']=0
data['Southeast Asia']=0
data['Eastern Europe']=0
data['Western Europe']=0
data['Africa']=0
print(data.head())

nrows = len(data.iloc[:,0])

for i in range(nrows):
    region = data["UnitedStates"][i] + data["Canada"][i] + data["Mexico"][i] + data["PuertoRico"][i] + data["Bahamas"][i] + data["CostaRica"][i] + data["Barbados"][i] + data["DominicanRepublic"][i]
    data.loc[i, 'North America'] = region
print(data.head())


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["Peru"][i] + data["Colombia"][i] + data["Venezuela"][i] + data["Belize"][i] + data["DominicanRepublic"][i]
    data.loc[i, 'South America'] = region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["India"][i] + data["Pakistan"][i] + data["Bangladesh"][i] 
    data.loc[i, 'South Asia']= region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["China"][i] + data["Taiwan"][i] + data["RepublicofKorea"][i] + data["HongKong"][i]  
    data.loc[i, 'East Asia'] = region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["Philippines"][i] + data["Vietnam"][i] + data["Malaysia"][i]   
    data.loc[i, 'Southeast Asia'] = region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["Ukraine"][i] + data["Bulgaria"][i] + data["Romania"][i] + data["Turkey"][i]     
    data.loc[i, 'Eastern Europe'] = region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region = data["Spain"][i] + data["Sweden"][i] + data["Netherlands"][i] + data["Austria"][i] + data["Denmark"][i] + data["Germany"][i] + data["Switzerland"][i] + data["Italy"][i]  + data["Ireland"][i]  + data["Portugal"][i] + data["UnitedKingdom"][i]
    data.loc[i, 'Western Europe'] = region


nrows = len(data.iloc[:,0])
for i in range(nrows):
    region =data["Somalia"][i] + data["Egypt"][i]
    data.loc[i, 'Africa'] = region

print(data.head())

data = data.drop(columns=["UnitedStates","India","China","Philippines","Canada","Bangladesh","Denmark","Germany","Mexico","Romania","Pakistan","Taiwan","Sweden","PuertoRico","Netherlands","Spain","Switzerland","Italy","Peru","Colombia","RepublicofKorea","Turkey","Egypt","Vietnam","Austria","HongKong","Portugal","Malaysia","Ireland","Ukraine","Bulgaria","Somalia","Bahamas","Venezuela","Belize","UnitedKingdom","CostaRica","DominicanRepublic","Barbados"], axis=1)
data = data.drop(columns=["Hour00","Hour01","Hour02","Hour03","Hour04","Hour05","Hour06","Hour07","Hour08","Hour09","Hour10","Hour11","Hour12","Hour13","Hour14","Hour15","Hour16","Hour17","Hour18","Hour19","Hour20","Hour21","Hour22","Hour23"], axis=1)
print(data)

# test = pd.read_csv("training.csv", index_col = 0)
# print(test)

testing_frame=data.iloc[:, :]
loaded_module = pickle.load(open("Retrained_model.sav", 'rb'))
predictions = loaded_module.predict(testing_frame)
print(predictions)

index = 0
msg_string = ''
for prediction in predictions:
    if prediction == -1:
        msg_string =  msg_string + "\n " + str(testing_frame.iloc[index, :])
    index += 1
print(len(msg_string))
msg_string = msg_string.replace(",", " ")
msg_string = msg_string.replace(":", " ")
db = mysql.connector.connect(host='localhost',
                            database='project',
                            user='root',
                            password='root'
                            )

mycursor = db.cursor()
mycursor.execute("INSERT INTO new_message SET message = '" + msg_string + "', receiver = 'paul', sender = 'robot';")
db.commit()





# myresult = mycursor.fetchall()


# def insertPythonVaribleInTable(suscriberId, region, time, browser):
#     sql_insert_query = """ INSERT INTO `pytest`
#                           (`suscriberid`, `region`, `time`, `browser`) VALUES (%s,%s,%s,%s)"""
#                 result  = cursor.execute(sql_insert_query)
#         connection.commit()
#         print ("Record inserted successfully into python_users table")
    