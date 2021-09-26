#-------------------------------------------------------------------------
# AUTHOR: Anthony Spencer
# FILENAME: naive_bayes.py
# SPECIFICATION: naive  Beyes file for class
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data
trainingDB=[]
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         trainingDB.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X=[]
for i in range(len(trainingDB)):
    column = []
    for j in range(len(trainingDB[i])-1):
      if trainingDB[i][j] == 'Sunny' or trainingDB[i][j] == 'Hot' or trainingDB[i][j] == 'High' or trainingDB[i][j] == 'Weak':
        column.append(1)
      elif trainingDB[i][j] == 'Overcast' or trainingDB[i][j] == 'Mild' or trainingDB[i][j] == 'Normal' or trainingDB[i][j] == 'Strong':
        column.append(2)
      elif trainingDB[i][j] =='Rain'or trainingDB[i][j] == 'Cool':
        column.append(3)
    X.append(column)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for i in range(len(trainingDB)):
    if trainingDB[i][len(trainingDB[i])-1]=='No':
        Y.append(2)
    else:
        Y.append(1)
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
testDB=[]
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         testDB.append (row)
Z=[]
for i in range(len(testDB)):
    column = []
    for j in range(len(testDB[i])-1):
      if testDB[i][j] == 'Sunny' or testDB[i][j] == 'Hot' or testDB[i][j] == 'High' or testDB[i][j] == 'Weak':
        column.append(float(1))
      elif testDB[i][j] == 'Overcast' or testDB[i][j] == 'Mild' or testDB[i][j] == 'Normal' or testDB[i][j] == 'Strong':
        column.append(float(2))
      elif testDB[i][j] =='Rain'or testDB[i][j] == 'Cool':
        column.append(float(3))
    Z.append(column)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
for i in range (len(Z)):
    predicted = clf.predict_proba([Z[i]])[0]
    if predicted[0] > .75:
        string = testDB[i][0].ljust(15)
        if Z[i][0]==1:
            string = string + "Sunny".ljust(15)
        elif Z[i][0]==2:
            string = string + "Overcast".ljust(15)
        elif Z[i][0]==3:
            string = string + "Rain".ljust(15)

        if Z[i][1]==1:
            string = string + "Hot".ljust(15)
        elif Z[i][1]==2:
            string = string + "Mild".ljust(15)
        elif Z[i][1]==3:
            string = string + "Cool".ljust(15)

        if Z[i][2]==1:
            string = string + "High".ljust(15)
        elif Z[i][2]==2:
            string = string + "Normal".ljust(15)

        if Z[i][2]==1:
            string = string + "Weak".ljust(15)
        elif Z[i][2]==2:
            string = string + "Strong".ljust(15)
        string = string + "Yes".ljust(15)
        string = string + str(predicted[0])
        print(string)
    if predicted[1] > .75:
        string = testDB[i][0].ljust(15)
        if Z[i][0]==1:
            string = string + "Sunny".ljust(15)
        elif Z[i][0]==2:
            string = string + "Overcast".ljust(15)
        elif Z[i][0]==3:
            string = string + "Rain".ljust(15)

        if Z[i][1]==1:
            string = string + "Hot".ljust(15)
        elif Z[i][1]==2:
            string = string + "Mild".ljust(15)
        elif Z[i][1]==3:
            string = string + "Cool".ljust(15)

        if Z[i][2]==1:
            string = string + "High".ljust(15)
        elif Z[i][2]==2:
            string = string + "Normal".ljust(15)

        if Z[i][2]==1:
            string = string + "Weak".ljust(15)
        elif Z[i][2]==2:
            string = string + "Strong".ljust(15)
        string = string + "No".ljust(15)
        string = string + str(predicted[1])
        print(string)
        


