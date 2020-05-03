# Titanic Survival Prediction


## Imported all the required library
```
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

```
### Loading the data

~~~
data=pd.read_csv('titanic_data.csv')
data.head()

## Data filling

~~~
clean_test.Age = clean_test.Age.fillna(titanic_data['Age'].mean())
testing_data.Fare=testing_data.Fare.fillna(data.Fare.mean())
~~~

# Using Different Model's 

## Creating Training and Testing Data set

~~~
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

~~~
# Training the model

~~~
model=LogisticRegression()
model.fit(x_train,y_train)
~~~
# Making the prediction

~~~
new_prediction=model.predict(testing_data)
~~~
## Getting the accuracy score

~~~
from sklearn.metrics import accuracy_score


acc_logreg = round(accuracy_score(prediction, y_test) * 100, 2)
print(acc_logreg)
~~~
